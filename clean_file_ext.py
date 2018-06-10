#clean up file paths in bing search
#Usage: python clean_file_ext.py --path dataset
import os
import re
import argparse


if __name__ == '__main__':

  ap = argparse.ArgumentParser()
  ap.add_argument("-in", "--path", required=True,
    help="Clean up file paths with unnecessary extesions from Bing Search")
args = vars(ap.parse_args())
path = args["path"]

filenames = os.listdir(path)

i = 0
for filename in filenames:
			file, ext = os.path.splitext(filename)
			if len(ext.split("?")) > 1:
				print("Modifying ", filename, "extension")
				outfilename = file + ext.split("?")[0]
				os.rename(os.path.join(path, filename), os.path.join(path, outfilename))
				i +=1

print(" Modified ", i, " files with messy extension")