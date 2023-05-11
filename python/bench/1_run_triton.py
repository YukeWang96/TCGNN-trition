#!/usr/bin/env python3
import numpy as np 
import os
os.environ["PYTHONWARNINGS"] = "ignore"
from scipy import sparse, io
import subprocess

hidden = 16
tile_size = 4096

hidden = 16
block_density = 0.1
block_scale = 1 / block_density
tile_size = 512

dataset = [        
        ( 'amazon0505'          , 410236  , 4878875),
        ( 'artist'              , 50515	  , 1638396),
        ( 'com-amazon'          , 548551  , 1851744),
        ( 'soc-BlogCatalog'	, 88784	  , 2093195),      
        ( 'amazon0601'  	, 403394  , 3387388), 
]

for data, node, edges in dataset:
    print("dataset={}".format(data))
    ntimes = edges * block_scale / (tile_size * tile_size) 
    result = subprocess.run(["python", "bench_blocksparse.py"], stdout=subprocess.PIPE)
    output = result.stdout.decode()
    res = float(output.rstrip("\n")) * ntimes
    print("Time (ms): {:.3f}".format(res))