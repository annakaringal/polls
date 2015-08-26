// Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

angular.module('pollsApp.services', ['ngResource'])
    .factory('User', function($resource) {
        return $resource(
            '/api/users/:id/',
            {
                id: "@id"
            },
            {
                update: {
                    method: "PUT"
                }
            }
        );

    })
    .factory('Polls', function($resource) {
        return $resource('/api/polls/:id/');
    });
