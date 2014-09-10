(function() {
  'use strict';
  var MainCtrl, myApp;

  myApp = angular.module('app', []);

  MainCtrl = function($scope) {
    return $scope.name = 'angular.js';
  };

  myApp.controller('MainCtrl', MainCtrl);

}).call(this);
