'use strict'

myApp = angular.module('app', [])

MainCtrl = ($scope) ->
  $scope.name = 'angular.js'

myApp.controller 'MainCtrl', MainCtrl
