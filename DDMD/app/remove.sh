#!/bin/sh
(ddmd) MacBook-Air-(2):datasets eshakya@unomaha.edu$ cd all_images
(ddmd) MacBook-Air-(2):all_images eshakya@unomaha.edu$ rm -rf *
(ddmd) MacBook-Air-(2):all_images eshakya@unomaha.edu$ cd ../../datasets/image_desc_joined/
(ddmd) MacBook-Air-(2):image_desc_joined eshakya@unomaha.edu$ rm -rf *
(ddmd) MacBook-Air-(2):image_desc_joined eshakya@unomaha.edu$ cd ../../datasets/image_description
(ddmd) MacBook-Air-(2):image_description eshakya@unomaha.edu$ rm -rf *
(ddmd) MacBook-Air-(2):image_description eshakya@unomaha.edu$ cd ../../datasets/image_description_paperwise/
(ddmd) MacBook-Air-(2):image_description_paperwise eshakya@unomaha.edu$ rm -rf *
(ddmd) MacBook-Air-(2):image_description_paperwise eshakya@unomaha.edu$ cd ../../datasets/images/
(ddmd) MacBook-Air-(2):images eshakya@unomaha.edu$ rm -rf *
(ddmd) MacBook-Air-(2):images eshakya@unomaha.edu$ cd ../../datasets/papers/
(ddmd) MacBook-Air-(2):papers eshakya@unomaha.edu$ rm -rf *
(ddmd) MacBook-Air-(2):papers eshakya@unomaha.edu$ cd ../../datasets/txt/
(ddmd) MacBook-Air-(2):txt eshakya@unomaha.edu$ rm -rf *
(ddmd) MacBook-Air-(2):txt eshakya@unomaha.edu$ cd ..
(ddmd) MacBook-Air-(2):datasets eshakya@unomaha.edu$ truncate -s 0 all_images.txt
bash: truncate: command not found
(ddmd) MacBook-Air-(2):datasets eshakya@unomaha.edu$ >all_images.txt
(ddmd) MacBook-Air-(2):datasets eshakya@unomaha.edu$ >captions.token.txt
(ddmd) MacBook-Air-(2):datasets eshakya@unomaha.edu$ >ddmd.token.txt
(ddmd) MacBook-Air-(2):datasets eshakya@unomaha.edu$ >error_pdf2txt.txt
(ddmd) MacBook-Air-(2):datasets eshakya@unomaha.edu$
