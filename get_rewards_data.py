#!/usr/bin/env python3

import subprocess
import csv
import os
from glob import glob
import re
import time

my_images_path = './screenshots'
image_files = glob(my_images_path + '/*.png')

for image_file in image_files:
    # tesseract automatically appends ".txt to the output file so just using same name as image for prefix"
    # -psm 6 was working well in testing. page segment mode 
    subprocess.call(['tesseract', image_file, image_file, '-psm', '6'])

# get the output txt files
files = glob(my_images_path + "/*.txt")

data = []
# get all the tesseract output
for filename in files: 
    data += open(filename, 'r').readlines()    

# each relevant line will start with a date, does not need to be perfect pattern here
pat = re.compile("^\d\d?/") 

# remove dollar signs and only take relevant lines
data = [line.replace("$","").split() for line in data if re.match(pat, line)]

with open('rewards{0}.csv'.format(time.strftime("%Y%m%d-%H%M%S")), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
# cleanup files
for f in files:
    os.remove(f)