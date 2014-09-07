import sockjs.tornado
from shared.rabbit import RabbitConsumer


class ChatHandler(sockjs.tornado.SockJSConnection):
    """Chat connection implementation"""
    # Class level variable
    participants = set()

    def on_open(self, info):
        """
        Triggered when a new client/participants joins.
        Subscribes to the rabbit consumer.
        Ands this client to the current list of active participants
        """
        self.broadcast(self.participants, "Someone joined.")

        consumer = RabbitConsumer('amqp://guest:guest@localhost:5672/%2F', self.on_rabbit_meessage)
        consumer.connect()
        # Add client to the clients list
        self.participants.add(self)

    def on_message(self, message):
        """
        Triggered for a messages coming from client.
        """
        # Broadcast message to all current participants
        self.broadcast(self.participants, message)

    def on_rabbit_meessage(self, body):
        """
        Triggered for a messages coming from rabbit.
        """
        # Broadcast message to all current participants
        self.broadcast(self.participants, body)

    def on_close(self):
        # Remove client from the clients list and broadcast leave message
        self.participants.remove(self)

        self.broadcast(self.participants, "Someone left.")

