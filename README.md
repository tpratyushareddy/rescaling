# Resource watcher

Monitors CPU and memory resources on the host and lets you resize the instance type if it exceeds the threshold limit.

### Installations required for the program:

Things to install
Python : pip install python or pip3 install python (to run the script in python)
Yaml   : pip install Yaml (For writing config files)
Psutil : pip install pstuil (for checking cpu/ memory usage)

### Config file:

Users can chnage the thressholds limit in [Config.yml](https://github.com/tpratyushareddy/rescaling/blob/main/config.yml).

### To run the python script:

Users can run python code directly by using the following command.
In command promt : python3 cpu_usage_display.py  

### To run in docker:

Using docker use the following command.
In command promt : docker run pratyusha056/rescaling:latest  

### Expected output:

It is set to display the CPU/Memory usage of the host system.
Breaks the loop if it reaches the threshold set in config file. 

### Note:

This project is automated to build images when ever there is a push to the 'main' branch. 
Meaning it automaticaly builds an image with the latest code change and provides the users 
with latest code and chnages. View [docker_image.yaml](https://github.com/tpratyushareddy/rescaling/blob/main/.github/workflows/docker_image.yml).

Check the [action file](https://github.com/tpratyushareddy/rescaling/actions). 
