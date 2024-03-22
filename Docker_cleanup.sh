#!/bin/sh

action = $1
if [ "$action" == [images] ]
then
    echo "Removing Images"
    docker rmi -f $(docker images -q)
elif [ "$action" == [container] ]
then
    echo "Removing Containers"
    docker rm -f $(docker ps -aq)
else 
    echo "Aurgumrent that has been passed is not valid, Please choose images or containers."
fi