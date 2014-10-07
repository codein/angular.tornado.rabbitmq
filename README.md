angular.tornado.rabbitmq
========================

A web app starter repo. Application stack consists of stubs for front and backend, also includes minimum wiring for achieving push notification over websockets.

### Front-end
A basic single page web app implementation using bootstraps, angular.js and coffeescript.

### Back-end
Tornado server to server static assets, handles the `/chat` enpoint to server push notifications.

#### Push notifications
The back-end sub-system can push messages to front end over websocket via rabbitmq messaging queues.

![gif] (https://raw.githubusercontent.com/codein/angular.tornado.rabbitmq/master/terminal.gif)
