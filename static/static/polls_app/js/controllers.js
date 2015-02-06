var pollsControllers = angular.module('pollsApp.controllers', []);

pollsControllers.controller('homeCtrl', function homeCtrl($scope, $filter, Polls) {

    $scope.all_polls = Polls;
    Polls.query(function(response){
       $scope.all_polls = response;
    });

});

pollsControllers.controller('UserCtrl', function UserCtrl($scope, $stateParams, User, AuthUser) {
    id = AuthUser.id;
    User.get({id:id}, function(response) {
        $scope.user = response;
    });
});

pollsControllers.controller('UserListingCtrl', function UserListingCtrl($scope, User) {
    $scope.users = User;
    User.query(function(response) {
        $scope.users = response;
    });
});

pollsControllers.controller('createUserCtrl', function createUserCtrl($scope, $state, User) {
    $scope.new_user = new User();

    $scope.addUser = function(){
        $scope.new_user.$save(function(){
            $state.go('userListing');
        });
    }
});
pollsControllers.controller('updateUserCtrl', function updateUserCtrl($scope, $stateParams, $state, User) {
    $scope.new_user = User.get({id:$stateParams.id});

    $scope.updateUser = function(){
        $scope.new_user.$update(function(){
            $state.go('userListing');
        });
    }
});