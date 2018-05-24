"""
Simple alphabetical cipher

This is a simple alphabetical shift encypter. Enter -1 or 1 for the direction,
your desired shift and laslty, the text to cipher.
   Written by Sami Dena (aurlit@riseup.net)
"""

import sys

def cipher(direction, shift, text):
    order = direction * shift
    return ','.join([str(ord(i) + order) for i in text])


def decipher(direction, shift, text):
    order = direction * shift
    return ''.join([chr(int(i) - order) for i in text.split(',')])


if __name__ == '__main__':
  
  if(len(sys.argv) == 4):
      encrypted_string = cipher(int(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3])) 
      print(encrypted_string)
      print(decipher(int(sys.argv[1]), int(sys.argv[2]), encrypted_string))
  else:
    print("Syntax Error: CaesarCipher [direction] [shift#] [text]")