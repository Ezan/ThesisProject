#!/usr/bin/env python
# -*- coding: utf-8 -*-  
"""
Created on Wed Mar 18 09:57:49 2020

@author: sindhu

This script extracts the Image Description from teh research papers.
Step 1: Convert all the research papers from pdf format to text format using external conversion tools or by writing a python script.
Step 2: place the text files in a directory(input path)
Step 3: Create a directory to save the extracted description (output path)

"""
def extract():
    import os
    import sys
    import re
    in_path = '../../datasets/txt'  #input path
    imagedesc_path = '../../datasets/image_description'  ##image description extracted path

    #reference: https://stackoverflow.com/questions/18865058/extract-values-between-two-strings-in-a-text-file-using-python

    current_line = ""
    for filename in os.listdir(in_path):
        full_file = os.path.join(in_path, filename)
        imagedesc_file = os.path.join(imagedesc_path, filename)
        with open(full_file, 'r') as infile, open(imagedesc_file, 'w') as outfile:   # Need to give encoding="utf-8" argument as well during reading or writing files while running in local windows machine other wise it throws errors like ""UnicodeEncodeError: 'charmap' codec can't encode character '\u2013",since there are some files with some nonreadable characters
            copy = False
            for line in infile:
                line_lower=line.lower()
                if line_lower.startswith('figure') or line_lower.startswith('fig'): # when the first word is figure,add that line to current_line,for the next line after this,it will jump to elif copy and there it conactenates all the next lines with the current_line
                    copy = True
                    outfile.write("\n") #if we dont add next line character to the file,other figure line is also getting conatenated to the previous line
                    line = line.replace('\n', ' ') #replace the next line character with space,so that we can contenate the lines to a single line
                    current_line=line
                    continue
                elif len(line.strip()) == 0:
            #outfile.writelines((line.encode('utf-8') for line in current_line))
                    outfile.write(current_line) # write the concatenated figure line to the file
                    current_line = ""
                    copy = False
                    continue
                elif copy:
                    line = line.replace('\n', ' ')
                    current_line=current_line+line


    """templine = currentline +'\n'
    #print(templine)
    temp = temp + templine
    print(temp)
    outfile.write(temp) """

# if __name__ == "__main__":
#     extract()








