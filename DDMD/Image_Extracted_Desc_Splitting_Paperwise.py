#!/usr/bin/env python
# -*- coding: utf-8 -*-  

# Without the above two lines,it is throwing below error when ran in server as it is python 2.7.17
# "SyntaxError: Non-ASCII character '\x96' in file Image_Extracted_Desc_Splitting_Paperwise.py on line 104, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details"

# =============================================================================
# Created on Mon Mar 30 10:05:43 2020
# @author: Jaya Sindhura Pailla
# 
# This script splits the IMage description into multiple lines like below
# input : Figure 1: (a)..... (b)......(c)......(d).....
# output:
# Figure 1:
# (a).....
# (b).....
# (c).....
# (d).....
# 
# Add encoding="utf-8" while reading or writing into the files ,when the code is ran out of the server
# In unix server encoding="utf-8" is not yielding proper results,so adding encoding="Latin-1"
# =============================================================================

import io
import os
import sys
import re

in_path = './datasets/image_description'  # image description extracted path
out_path = './datasets/image_description_paperwise'  # image description split path

for filename in os.listdir(in_path):
    print(filename)
    # %%Code to split data of paper: 01-2D_materials_-_ACS_Nano.txt
    if filename == '01-2D_materials_-_ACS_Nano.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Figure [0-9]\.', line) or re.match('Figure [0-9][0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\)|\([a-z],[a-z]\))',
                                              line)  # split the lines based on (a) or (b) etc or(a,b) etc
                        for item in split_list:
                            if re.match('Figure [0-9]\.', item) or re.match('Figure [0-9][0-9]\.', item) or re.match(
                                    '\([a-z]\) |\([a-z],[a-z]\) ', item):
                                if re.match('Figure 14. In particular,',
                                            item):  # figure 14. is present even in the file apart from figure description,so ignoring it
                                    print('ignore this line')
                                else:
                                    outfile.write("%s\n" % item)  # to write each item of a list to the file
                                    # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 02-ali1968.txt.
    # Ignore this file as the entire paper is scanned,so we cannot extract images from scanned paper
    # %%Code to extract data from paper: 03-Complete_Corrosion_Inhibition_through_Graphene_.txt
    if filename == '03-Complete_Corrosion_Inhibition_through_Graphene_.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Figure [0-9]\.', line) or re.match('Figure [0-9][0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\)|\([a-z],[a-z]\))',
                                              line)  # split the lines based on (a) or (b) etc or(a,b) etc
                        for item in split_list:
                            if re.match('Figure [0-9]\.', item) or re.match('Figure [0-9][0-9]\.', item) or re.match(
                                    '\([a-z]\) |\([a-z],[a-z]\) ', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 04-copper_CZ_process.txt
    if filename == '04-copper_CZ_process.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Figure [0-9]\.', line) or re.match('Figure [0-9][0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\)|\([a-z],[a-z]\))',
                                              line)  # split the lines based on (a) or (b) etc or(a,b) etc
                        for item in split_list:
                            if re.match('Figure [0-9]\.', item) or re.match('Figure [0-9][0-9]\.', item) or re.match(
                                    '\([a-z]\) |\([a-z],[a-z]\) ', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 06-Cu_Oxdns_ncln_sites_acs.txt
    if filename == '06-Cu_Oxdns_ncln_sites_acs.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Figure [0-9]\.', line) or re.match('Figure [0-9][0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\)|\([a-z], [a-z]\))',
                                              line)  # split the lines based on (a) or (b) etc or(a,b) etc
                        for item in split_list:
                            if re.match('Figure [0-9]\.', item) or re.match('Figure [0-9][0-9]\.', item) or re.match(
                                    '\([a-z]\) |\([a-z], [a-z]\) ', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 07-Cu_Stress-response-Staph-AEM-2010-Baker.txt
    if filename == '07-Cu_Stress-response-Staph-AEM-2010-Baker.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('FIG. [0-9]\.', line) or re.match('FIG. [0-9][0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([A-Z]\)|\([A-Z], [A-Z]\))',
                                              line)  # split the lines based on (a) or (b) etc or(a,b) etc
                        for item in split_list:
                            if re.match('FIG. [0-9]\.', line) or re.match('FIG. [0-9][0-9]\.', line) or re.match(
                                    '.(?=\([A-Z]\)|\([A-Z], [A-Z]\))', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 09-CVD_growth__Nature_Materials_.txt
    if filename == '09-CVD_growth__Nature_Materials_.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Fig. [0-9]', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\. [a-z]–[a-z],|\. [a-z],)',
                                              line)  # split the lines based on (a) or (b) etc or(a,b) etc
                        for item in split_list:
                            if re.match('Fig. [0-9]', line) or re.match('.(?=\. [a-z]–[a-z],|\. [a-z],)', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 10-effect_of_crystallographic_orientation_on_corro.txt
    # ignore the spaces in the words as the paper is very old and the format is different
    if filename == '10-effect_of_crystallographic_orientation_on_corro.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Fig. [0-9]', line):
                    outfile.write("%s" % line)  # to write each item of a list to the file
                    # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 11-Electronic_structure_of_graphene-hexagonal_boro.txt
    if filename == '11-Electronic_structure_of_graphene-hexagonal_boro.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding="utf-8") as infile, io.open(imagedesc_split_file, 'w',
                                                                          encoding="utf-8") as outfile:
            for line in infile:
                if re.match('Figure [0-9]', line):
                    if line.strip():
                        split_list = re.split(r'.(?= [a-z],)',
                                              line)  # split the lines based on (a) or (b) etc or(a,b) etc
                        for item in split_list:
                            if re.match('Figure [0-9]', line) or re.match('.(?= [a-z],)', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                            # outfile.write('\n') #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 12-Epitaxial_Graphene_on_Cu_111_.txt
    if filename == '12-Epitaxial_Graphene_on_Cu_111_.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('FIGURE [0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\) [A-Z])',
                                              line)  # Added [A-Z] in order to split based on "(a) The....." etc just to avaoid splite (a) and (b) etc
                        for item in split_list:
                            if re.match('FIGURE [0-9]\.', line) or re.match('.(?=\([a-z]\) [A-Z])', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 13-Graphene, hexagonal boron nitride, and their
    if filename == '13-Graphene, hexagonal boron nitride, and their.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            concat = " ".join(line.rstrip('\n') for line in
                              infile)  # files 13,14, &24 have pdf to .txt conversion issues ,so adding these 2 lines to merge all the lines first and then split them based on "fig"
            split_list = re.split(r'.(?=Fig.)', concat)
            for line in split_list:
                if re.match('Fig. [0-9] |Fig.  [0-9] |Fig. [0-9][0-9] |Fig.  [0-9][0-9] |Fig.   [0-9][0-9] ', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\. \([a-z]\)–\([a-z]\) |\([a-z]\)|\([A-Z]\)|\([a-z] and [a-z]\))',
                                              line)  # This \([a-z]\)Â\([a-z]\) is not working.eg:(a)-(b) is not getting split.Need to see at later point of time
                        for item in split_list:
                            if re.match(
                                    'Fig. [0-9] |Fig.  [0-9] |Fig. [0-9][0-9] |Fig.  [0-9][0-9] |Fig.   [0-9][0-9] ',
                                    line) or re.match(
                                    '.(?=\. \([a-z]\)Â\([a-z]\) |\([a-z]\)|\([A-Z]\)|\([a-z] and [a-z]\))', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure

    # %%Code to split data of paper: 14-Growth of epitaxial graphene- Theory and experiment
    if filename == '14-Growth of epitaxial graphene- Theory and experiment.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            concat = " ".join(line.rstrip('\n') for line in
                              infile)  # files 13,14, &24 have pdf to .txt conversion issues ,so adding these 2 lines to merge all the lines first and then split them based on "fig"
            split_list = re.split(r'.(?=Fig.)', concat)
            for line in split_list:
                if re.match('Fig. [0-9]\.|Fig. [0-9][0-9]\.', line):
                    line_replace = line.replace('((', '{{').replace('))',
                                                                    '}}')  # eg((b)-(d)) for these the data is not getting split,as the split function is giving priority the regular exp \([a-z]\) over \(\([a-z]\)\),that's why replacing (()) with {{}} to distincguish
                    if line_replace.strip():
                        split_list = re.split(r'.(?=\{\{[a-z]\)–\([a-z]\}\}|\([a-z]\)|\([a-z]–[a-z]\))',
                                              line_replace)  # Added [A-Z] in order to split based on "(a) The....." etc just to avaoid splite (a) and (b) etc
                        for item in split_list:
                            if re.match('Fig. [0-9]\.|Fig. [0-9][0-9]\.', line) or re.match(
                                    '.(?=\{\{[a-z]\)–\([a-z]\}\}|\([a-z]\)|\([a-z]–[a-z]\))', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 15-Impact_of_electrolyte_intercalation_on_the_corr.txt
    if filename == '15-Impact_of_electrolyte_intercalation_on_the_corr.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Fig. [0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\) [A-Z])',
                                              line)  # Added [A-Z] in order to split based on "(a) The....." etc just to avaoid splite (a) and (b) etc
                        for item in split_list:
                            if re.match('Fig. [0-9]\.', line) or re.match('.(?=\([a-z]\) [A-Z])', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 16-Influence_of_lattice_orientation_on_growth_and_.txt
    # Not doing any splitting based on (a),(b) etc as each image is correlated amin themsleves and individual explanation is not provided
    if filename == '16-Influence_of_lattice_orientation_on_growth_and_.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                outfile.write("%s" % line)  # to write each item of a list to the file
                ##outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 17-Interface_Formation_in_Monolayer_Graphene-Boron.txt
    if filename == '17-Interface_Formation_in_Monolayer_Graphene-Boron.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Figure [0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\) )',
                                              line)  # Added [A-Z] in order to split based on "(a) The....." etc just to avaoid splite (a) and (b) etc
                        for item in split_list:
                            if re.match('Figure [0-9]\.', line) or re.match('.(?=\([a-z]\) )', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 19-Observing_Graphene_Grow_Catalyst_Graphene_Inter.txt
    if filename == '19-Observing_Graphene_Grow_Catalyst_Graphene_Inter.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Figure [0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\) )',
                                              line)  # Added [A-Z] in order to split based on "(a) The....." etc just to avaoid splite (a) and (b) etc
                        for item in split_list:
                            if re.match('Figure [0-9]\.', line) or re.match('.(?=\([a-z]\) )', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 20-oles_of_Oxygen_and_Hydrogen_in_Crystal_Orientat.txt
    if filename == '20-oles_of_Oxygen_and_Hydrogen_in_Crystal_Orientat.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Figure [0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\) |\. \([a-z]–[a-z]\))',
                                              line)  # Added [A-Z] in order to split based on "(a) The....." etc just to avaoid splite (a) and (b) etc
                        for item in split_list:
                            if re.match('Figure [0-9]\.', line) or re.match('.(?=\([a-z]\) |\. \([a-z]–[a-z]\))', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 21-Oxdn_bhvr_Gr-cu_dfcts_Nat.txt
    if filename == '21-Oxdn_bhvr_Gr-cu_dfcts_Nat.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Fig. [0-9] ', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\. [a-z] |\, [a-z] | [a-z] and [a-z] | [a-z]–[a-z])',
                                              line)  # Added [A-Z] in order to split based on "(a) The....." etc just to avaoid splite (a) and (b) etc
                        for item in split_list:
                            if re.match('Fig. [0-9]', line) or re.match(
                                    '.(?=\. [a-z] |\, [a-z] | [a-z] and [a-z] | [a-z]–[a-z])', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure

    # %%Code to split data of paper: 22-srep45358.txt
    if filename == '22-srep45358.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('Figure [0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\)|\([a-z]–[a-z]\) |;)',
                                              line)  # Added [A-Z] in order to split based on "(a) The....." etc just to avaoid splite (a) and (b) etc
                        for item in split_list:
                            if re.match('Figure [0-9]\.', line) or re.match('.(?=\([a-z]\)|\([a-z]–[a-z]\) |;)', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 23-Substrate_grain_size_and_orientation_of_Cu_and_.txt
    if filename == '23-Substrate_grain_size_and_orientation_of_Cu_and_.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            for line in infile:
                if re.match('FIG. [0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\))',
                                              line)  # Added [A-Z] in order to split based on "(a) The....." etc just to avaoid splite (a) and (b) etc
                        for item in split_list:
                            if re.match('FIG. [0-9]\.', line) or re.match('.(?=\([a-z]\))', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
    # %%Code to split data of paper: 24-Thermal Growth of Graphene- A Review.txt
    if filename == '24-Thermal Growth of Graphene- A Review.txt':
        full_file = os.path.join(in_path, filename)
        imagedesc_split_file = os.path.join(out_path, filename)
        with io.open(full_file, 'r', encoding='Latin-1') as infile, io.open(imagedesc_split_file, 'w',
                                                                            encoding='Latin-1') as outfile:
            concat = " ".join(line.rstrip('\n') for line in
                              infile)  # files 13,14, &24 have pdf to .txt conversion issues ,so adding these 2 lines to merge all the lines first and then split them based on "figure"
            split_list = re.split(r'.(?=Figure)', concat)
            for line in split_list:
                if re.match('Figure [0-9]\.|Figure  [0-9]\.|Figure [0-9][0-9]\.|Figure  [0-9][0-9]\.', line):
                    if line.strip():
                        split_list = re.split(r'.(?=\([a-z]\)|\([a-z]–[a-z]\))',
                                              line)  # Added [A-Z] in order to split based on "(a) The....." etc just to avaoid splite (a) and (b) etc
                        for item in split_list:
                            if re.match('Figure [0-9]\.|Figure  [0-9]\.|Figure [0-9][0-9]\.|Figure  [0-9][0-9]\.',
                                        line) or re.match('.(?=\([a-z]\)|\([a-z]–[a-z]\))', item):
                                outfile.write("%s\n" % item)  # to write each item of a list to the file
                                # outfile.write("\n") #if we dont add next line character to the file,all the lines are loading into the same line of a particular figure
