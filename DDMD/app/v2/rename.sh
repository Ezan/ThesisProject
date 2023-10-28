#!/bin/sh
for file in ../datasets/PDFigCapx/*/*.{jpg,txt}
do
  fname=${file##*/} #This gives your base filename.
  fpath=${file%/*} # Your dir
  dname=${fpath##*/}
  mv $file ${fpath}/${dname}_${fname}
done