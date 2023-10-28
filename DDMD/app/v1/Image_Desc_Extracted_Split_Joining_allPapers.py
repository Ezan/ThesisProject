#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# =============================================================================
# Created on Fri Apr 10 10:05:43 2020
# @author: Jaya Sindhura Pailla
# 
# This script deos the following on the Image description that is being split already.
#input :
# Figure 1: 
# (a)..... 
# (b)......
# (c)......
# (d).....
#output:
# Figure 1 (a):.....
# Figure 1 (b):.....
# Figure 1 (c):.....
# Figure 1 (d):.....
# =============================================================================
def split_join():
    import io
    import os
    import sys
    import re
    in_path = '../../datasets/image_description_paperwise'  # image description extracted path
    out_path = '../../datasets/image_desc_joined'  # image description split path


    for filename in os.listdir(in_path):
        full_file = os.path.join(in_path, filename)
        imagedesc_file = os.path.join(out_path, filename)
        with open(full_file, 'r') as infile, open(imagedesc_file, 'w') as outfile:
            #print(infile)
            for line in infile:
                line_with_single_spaces = ' '.join(line.split()) #removing multiple spaces in the line
                line_lower=line_with_single_spaces.lower()
                #print(line_with_single_spaces)
                if line.strip(): #to avoid empty lines
                    if line_lower.startswith('figure') or line_lower.startswith('fig'):
                        try:
                          figure_number = re.match('(figure [0-9][0-9]\.|figure [0-9]\.|'
                                                     'figure. [0-9][0-9]\.|figure. [0-9]\.|'
                                                     'figure [0-9][0-9]|figure [0-9]|'
                                                     'fig [0-9][0-9]\.|fig [0-9]\.|'
                                                     'fig [0-9][0-9]|fig [0-9]|'
                                                     'fig. [0-9][0-9]\.|fig. [0-9]\.|'
                                                     'fig. [0-9][0-9]|fig. [0-9])',line_lower).group(1) #group(1) is to pick Figure 1 or 2 etc out of the matching string
                        except AttributeError:
                          figure_number = re.match('(figure [0-9][0-9]\.|figure [0-9]\.|'
                                                     'figure. [0-9][0-9]\.|figure. [0-9]\.|'
                                                     'figure [0-9][0-9]|figure [0-9]|'
                                                     'fig [0-9][0-9]\.|fig [0-9]\.|'
                                                     'fig [0-9][0-9]|fig [0-9]|'
                                                     'fig. [0-9][0-9]\.|fig. [0-9]\.|'
                                                     'fig. [0-9][0-9]|fig. [0-9])',line_lower) #group(1) is to pick Figure 1 or 2 etc out of the matching string

                        if len(line) > 15: #to avoid lines having just figure numbers without any data
                            line_space_between_puct_removed = re.sub('(?<=[.]) (?=[(])', '', line_with_single_spaces) #removing space between punctuation marks,eg i/p: figure 1. (a-c)  o/p:figure 1.(a-c)
                            line_space_between_puct_removed1 = re.sub(r'\(.*?\)', lambda x: ''.join(x.group(0).split()), line_space_between_puct_removed) #removing space with in the brackets,eg(Paper 16) i/p: (a, b, d)  o/p:figure 1.(a,b,d)
                            outfile.write(line_space_between_puct_removed1) # to write each item of a list to the file
                            outfile.write('\n')
                    else:
                        total_line = figure_number + line_with_single_spaces
                        line_space_between_puct_removed = re.sub(r'\(.*?\)', lambda x: ''.join(x.group(0).split()), total_line) #removing space with in the brackets,eg(Paper 6) i/p: figure 1. (a, c)  o/p:figure 1.(a,c)
                        line_space_between_puct_removed1 = re.sub('(?<=[.]) (?=[a-z],)', '', line_space_between_puct_removed) #removing space eg(Paper 9): i/p: figure 1. a,  o/p:figure 1.a,
                        #line_space_between_puct_removed2 = re.sub('(?<=[.]) (?=[a-z]]�)', '', line_space_between_puct_removed1) # Issue with "-" :so ignoring this for now removing space eg(Paper 9): i/p: figure 1. c-d,  o/p:figure 1.c-d,
                        line_space_between_puct_removed2 = re.sub('(?<=[.]) (?=[a-z] )', '', line_space_between_puct_removed1) #removing space eg(Paper 9): i/p: figure 1. a   o/p:figure 1.a
                        line_space_between_puct_removed3 = re.sub('(?<=[,]) (?=[a-z] )', '', line_space_between_puct_removed2) #removing space eg(Paper 9): i/p: figure 1, a   o/p:figure 1,a,
                        line_space_between_puct_removed4 = re.sub('(?<=[..]). (?=[(])', '', line_space_between_puct_removed3) #removing space eg(Paper 9): i/p: figure 1.. (a-b)   o/p:figure 1.(a-b)
                        outfile.write(line_space_between_puct_removed4)
                        outfile.write('\n')


# if __name__ == "__main__":
#     split_join()