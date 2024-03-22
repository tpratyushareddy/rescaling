#!/bin/sh


if [ "$1" == [images] ]
then
    echo "Removing Images"
    docker rmi -f $(docker images -q)
elif [ "$1" == [container] ]
then
    echo "Removing Containers"
    docker rm -f $(docker ps -aq)
else 
    echo "$1 that has been passed is not valid, Please choose images or containers."
fi