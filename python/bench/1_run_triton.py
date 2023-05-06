#!/usr/bin/env python3
import os
os.environ["PYTHONWARNINGS"] = "ignore"
import numpy as np 
from scipy import sparse, io
import subprocess

hidden = 16
tile_size = 16384

dataset = [
        ( 'amazon0505'          , 410236  , 22),
        ( 'artist'              , 50515	  , 12),
        ( 'com-amazon'          , 548551  , 22),
        ( 'soc-BlogCatalog'	, 88784	  , 39),      
        ( 'amazon0601'  	, 403394  , 22), 
]

for data, node, _ in dataset:
    print("dataset={}".format(data))
    ntimes = node * node / (tile_size * tile_size) 
    result = subprocess.run(["python", "bench_blocksparse.py"], stdout=subprocess.PIPE)
    output = result.stdout.decode()
    res = float(output.rstrip("\n")) * ntimes
    print("Time (ms): {:.3f}".format(res))