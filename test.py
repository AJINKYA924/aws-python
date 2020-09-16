#
# Python script to fetch system information
# 

import platform

# Architecture
print("Architecture: " + platform.architecture()[0])

# machine
print("Machine: " + platform.machine())

# node
print("Node: " + platform.node())

# processor
print("Processors: ")
with open("/proc/cpuinfo", "r")  as f:
    info = f.readlines()
cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
for index, item in enumerate(cpuinfo):
    print("    " + str(index) + ": " + item)

# system
print("System: " + platform.system())


# Memory
print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()

print("     " + lines[0].strip())
print("     " + lines[1].strip())

# Load
with open("/proc/loadavg", "r") as f:
    print("Average Load: " + f.read().strip())
