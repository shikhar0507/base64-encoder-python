# image-encoder-python

Encodes the file to base64,base16 or base32 format

### Installation
Run this file directly ```python base64Encoder.py```  
or
Make it as an executable for linux and unix systems  

```chmod +x base64Encoder.py ```

### How to use
1. **`--input`** : Input file location
2. **`--output`**: Output file name. Defaults to creating a file called ***encoded.txt*** in the same directory
3. **`--encoder`**: Encoder format base16,base32,base64. Defaults to base64
4. **`--open`**: If input file is an image file , it opens the encoded base64 content in browser. Supported image types are png, jpg , jpeg, webp, gif,tiff,bmp

#### Example
1. ```python base64Encoder.py --input image.png```
Outputs the encoded base64 to a file called ***encoded.txt***

2. ```python base64Encoder.py --input file.js --encoder base32 --output file-encoded.txt```
Outputs the encoded base32  to a file called ***file-encoded.txt***

3. ```python base64Encoder.py --input image.png  --open true```
Opens the encoded base64 string in the default web browser