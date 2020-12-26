#!/usr/bin/env python3
import base64;
import argparse;
import os;
import sys;
import webbrowser;

parser = argparse.ArgumentParser(description="Process encoding")
parser.add_argument("--input",type=str,help="Input file location")
parser.add_argument("--output",type=str,help="Ouput file name, defaults to creating a file called encoded.txt",default="encoded.txt")
parser.add_argument("--encoder",type=str,help="Encoder format, base16,base32,base64 defaults to base64",default="base64")
parser.add_argument("--open",help="If input file is an image file , it opens the encoded base64 content in browser. Supported image types are png, jpg , jpeg, webp, gif,tiff,bmp",default=False,type=bool)

args = parser.parse_args()
input_path = args.input
if input_path == None:
    sys.exit('Enter a valid input path')
if os.path.isfile(input_path) == False:
    sys.exit('Cannot find the specified file')

#Read file
file = open(input_path,"rb")

def encodeFile(file,format):
    if format == "base16":
        return base64.b16encode(file.read())
    if format == "base32":
        return base64.b32encode(file.read())
    if format == "base64":
        return base64.b64encode(file.read())
   
def isImageFile(path):
    extension = getExtension(path)
    extensions = ["png","jpg","jpeg","webp","gif","tiff","bmp"]
    try:
        return extensions.index(extension) > -1
    except ValueError as ve:
        return False

def getExtension(path):
    split = path.split(".")
    return split[len(split)-1]

encodedeOutput = encodeFile(file,args.encoder)
open(args.output,"wb").write(encodedeOutput)

if args.open == True:
    if isImageFile(input_path):
        webbrowser.open("data:image/"+getExtension(input_path)+";base64,"+encodedeOutput.decode("utf-8"))
    else:
        print("Only supported image files can be opened in browser")