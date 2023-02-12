# Author: 	Jure Novak
# Date:		12.02.2023

# This small Python script renames all files in a specified folder by their metadata date and time of creation.
# YYYYMMDD_HHMMSS.ext

import sys				
import exifread
import os

path = sys.argv[1]
for filename in os.listdir(path):
    with open(os.path.join(path, filename), 'rb') as f:
        tags = exifread.process_file(f)
        try:
            date_time = tags['EXIF DateTimeOriginal'].values
            base, ext = os.path.splitext(filename)
            new_file_name = date_time.replace(':', '').replace(' ', '_') + ext
        except KeyError:
            continue
    f.close()
    os.rename(os.path.join(path, filename), os.path.join(path, new_file_name))		