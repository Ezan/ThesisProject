# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 10:05:43 2020
@author: Jaya Sindhura

This script splits the IMage description into multiple lines like below
input : Figure 1: (a)..... (b)......(c)......(d).....
output:
Figure 1:
(a).....
(b).....
(c).....
(d).....
"""
def extract():
    import os
    import sys
    import re

    in_path = '../../datasets/image_description'  # image description extracted path
    out_path = '../../datasets/image_description_paperwise'  # image description split path

    for filename in os.listdir(in_path):
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with open(full_file, 'r') as infile, open(imagedesc_split_file, 'w') as outfile:   #encoding="utf-8" is not required in Putty where as it is required while running code outside puttty
            for line in infile:
               if line.strip():
                   a= re.split(r'.(?=\([a-z]\)|\([A-E]\)|\([a-z],[a-z]\)|\([a-z], [a-z]\)|\. [a-z],)', line) #split the lines based on (a) or (b) etc or(a,b) etc
                   for item in a:
                       outfile.write("%s" % item) # to write each item of a list to the file
                   #outfile.write("%s" % item.lower()) # can convert to lowercase while writng to the file if required.

                       outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
                   #print(item)

                    

# if __name__ == "__main__":
#     extract()


