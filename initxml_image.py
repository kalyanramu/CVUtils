#Example Usage: python initxml_image.py --input ./indata --output ./outdata

from gen_xml_utils import write_xml_voc
import argparse
import os
import cv2

if __name__ == '__main__':

  ap = argparse.ArgumentParser()
  ap.add_argument("-in", "--input", required=True,
    help="search query to search Bing Image API for")
  ap.add_argument("-out", "--output", required=True,
    help="path to output directory of images")
  args = vars(ap.parse_args())

  input_folder = args["input"]
  output_folder   = args["output"] 

  print("Input Folder: ", input_folder)
  print("Output Folder: ", output_folder)

  for n, img_name in enumerate(os.scandir(input_folder)):

    print("image_file" , str(n) , ": ", img_name.name)
    #Get image from 

    image = cv2.imread(img_name.path)
    height, width, depth = image.shape
    objects = ["timemag"]
    tl = [(0,0)]
    br = [(image.shape[0],image.shape[1])]    
    write_xml_voc(input_folder,img_name, objects, tl,br, output_folder)