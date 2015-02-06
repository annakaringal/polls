angular.module('pollsApp', [
    'ui.router',
    'ngResource',
    'pollsApp.services',
    'pollsApp.controllers'

])
    .config(function ($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $urlRouterProvider) {
        // Force angular to use square brackets for template tag
        // The alternative is using {% verbatim %}
        $interpolateProvider.startSymbol('[[').endSymbol(']]');

        // CSRF Support
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        // This only works in angular 3!
        // It makes dealing with Django slashes at the end of everything easier.
        $resourceProvider.defaults.stripTrailingSlashes = false;

        // Django expects jQuery like headers
        // $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';

        // Routing
        $urlRouterProvider.otherwise('/');
        $stateProvider
            .state('/', {
                url: '/',
                templateUrl: '../../static/polls_app/views/home.html',
                controller: 'homeCtrl'
            })
            .state('userListing', {
                url: '/users/',
                templateUrl: '../../static/polls_app/views/users/all.html',
                controller: 'UserListingCtrl'
            })
            .state('createUser', {
                url: '/users/create',
                templateUrl: '../../static/polls_app/views/users/create_user.tmpl.html',
                controller: 'createUserCtrl'
            })
            .state('updateUser', {
                url: '/users/:id/update',
                templateUrl: '../../static/polls_app/views/users/update_user.tmpl.html',
                controller: 'updateUserCtrl'
            })
    });