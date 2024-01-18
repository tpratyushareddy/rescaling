# Resource watcher

Monitors cpu and memory resources on the host and lets you resize the instance type if it expends the threshold limit.

### Installations required for the program  

Things to install
Python : pip install python or pip3 install python (to run the script in python)
Yaml   : pip install Yaml (For writing config files)
Psutil : pip install pstuil (for checking cpu/ memory usage)

### Config file

Has two parameters: Cpu_threshold and Memory_threshold

### How to run the program 

In command promt : python run cpu_usage_display.py  

### Expected output

It is set to display the CPU/Memory usage of the host system.
Breaks the loop if it reaches the threshold set in config file. 