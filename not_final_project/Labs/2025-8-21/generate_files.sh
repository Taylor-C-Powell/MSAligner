#!/bin/bash

# generate_files.sh
# This script creates a series of dummy files in the current directory.
# Each file will be named file_<i>.<ext> for i = 0..9 and ext in {txt, md, csv, tsv, rtf}
# It will overwrite any existing files with the same names.

echo "Creating dummy files..."

mkdir -p even_files odd_files

for i in {0..9}; do
  for ext in txt md csv tsv rtf; do
    filename="file_${i}.${ext}"
    echo "Creating ${filename}..."

    # Remove file if it already exists
    if [ -f "${filename}" ]; then
      rm "${filename}"
    fi

    # Create the file and add a simple header
    touch "${filename}"
    printf "# File index: ${i} | Extension: ${ext}\n" >> "${filename}"

    if (( i % 2 )); then
      mv -- "${filename}" odd_files/
    else
      mv -- "${filename}" even_files/
    fi
  done
done

echo "Done creating files."
pwd
ls -lh
