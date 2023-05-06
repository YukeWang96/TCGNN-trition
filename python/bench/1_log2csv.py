#!/usr/bin/env python3
import re
import sys 

if len(sys.argv) < 2:
    raise ValueError("Usage: ./1_log2csv.py result.log")

fp = open(sys.argv[1], "r")

dataset_li = []
time_li = []
for line in fp:
    if "dataset=" in line:
        data = line.split("=")[1].rstrip("\n").lstrip()
        print(data)
        dataset_li.append(data)
    if ":" in line:
        time = line.split(":")[1].rstrip("\n").lstrip()
        print(time)
        time_li.append(time.strip("ms"))
fp.close()

fout = open(sys.argv[1].strip(".log")+".csv", 'w')
fout.write("Dataset, Time (ms)\n")
for data, time in zip(dataset_li, time_li):
    fout.write("{},{}\n".format(data, time))
fout.close()
print("\n\n=>Check [{}] for results\n\n".format(sys.argv[1].strip(".log")+".csv"))