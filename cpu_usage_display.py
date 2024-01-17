import time
import psutil 
import yaml

#print(psutil.cpu_percent())
#print(psutil.virtual_memory().percent)

#with open('config.yaml', 'r') as file:
    #thresholds = yaml.safe_load(file)

#print(thresholds[prime_numbers]['0'])
#print(thresholds['mem_threshold'])

with open('config.yml', 'r') as file:
    prime_service = yaml.safe_load(file)

print(prime_service['prime_numbers'][0])
print(prime_service['rest']['url'])

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage/100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end = "")
    print(f"MEMORY USAGE:|{mem_bar}| {mem_usage:.2f}%  ", end = "\r")

while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)