import time
import psutil 
import yaml

print(psutil.cpu_percent())
print(psutil.virtual_memory().percent)

with open('config.yml', 'r') as file:
    data = yaml.safe_load(file)

cpu_t = data['thresholds']['cpu_threshold']
mem_t = data['thresholds']['mem_threshold']


def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage/100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end = "")
    print(f"MEMORY USAGE:|{mem_bar}| {mem_usage:.2f}%  ", end = "\r")

while True:
      cpu_usage = 0
      memory_usage = 0
      display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
      time.sleep(0.5)
      cpu_usage = psutil.cpu_percent()
      memory_usage = psutil.virtual_memory().percent
      if(cpu_usage >= cpu_t):
          print("Reached its CPU threshold limit")
          print("Crossed the CPU threshold limit of ", cpu_t)
          print("the current CPU usage is ", cpu_usage)
          break
      else:
          print("\r")
          print("Still within the limit")
    
      if(memory_usage >= mem_t):
          print("Reached its threshold limit")
          print("Crossed the memory threshold limit of ", mem_t)
          print("the current memory usage is ", memory_usage)
          break
      else:
          print("\r")
          print("Still within the limit")
    
