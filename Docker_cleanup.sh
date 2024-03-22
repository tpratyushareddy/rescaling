#!/bin/sh

action = $1
if [ $action -eq images ]
then
    echo "Removing Images"
    docker rmi -f $(docker images -q)
elif [ $action -eq container ]
then
    echo "Removing Containers"
    docker rm -f $(docker ps -aq)
else 
    echo "$action that has been passed is not valid."
    echo "Please choose images or containers." 

fi                         