#!/usr/bin/env python3

import subprocess
import csv
import os
import sys
import time

my_images_path = './screenshots'
image_files = [os.path.join(my_images_path, filename)
        for filename in os.listdir(my_images_path)
        if filename.endswith(".png")]

files = []
for image_file in image_files:
    subprocess.call(['tesseract', image_file, image_file, '-psm', '6'])
    # tesseract automatically appends ".txt to the output file so just using same name as image for prefix
    # -psm 6 was working well in testing. page segment mode
    files.append("{0}.txt".format(image_file))

data = []
for filename in files:
    data += open(filename, 'r').readlines()

# remove dollar signs and only take relevant lines
unique = set()
for record in data:
    if not record in unique:
        unique.add(record)

data = [line.replace("$","").split() for line in list(unique) if line.find('/') > 0]

csvname = os.path.join('./output', 'rewards{0}.csv'.format(time.strftime("%Y%m%d-%H%M%S")))

with open(csvname, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['date', 'reward', 'cumulative'])
    writer.writerows(data)

# cleanup files
for filename in files:
    os.remove(filename)

# import into pandas if you want a richer data structure
if len(sys.argv) <= 1 or sys.argv[1] != '-v':
    pass
elif sys.argv[1] == '-v':
    from analyze_rewards import dataframe_rewards
    dataframe_rewards(csvname)
