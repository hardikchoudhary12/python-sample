#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def get_special_paths(directory):
  filenames = os.listdir(directory)
  specialfilenames = []
  for filename in filenames:
    match = re.search("\_\_\w+\_\_",filename)
    if match:
      specialfilenames.append(filename)
  return specialfilenames

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    print ("since no parameter passed, printing special files in current directory")
    list_of_special_filenames = get_special_paths(os.getcwd())
    print(list_of_special_filenames)
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    #del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    #del args[0:2]

  if len(args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit(1)
  specialfilenames = get_special_paths(os.getcwd())
  if todir is not '':
  #copying and making directories
    os.makedirs(todir, exist_ok=True)
    for filename in specialfilenames:
      shutil.copy(os.getcwd() + "\\" + filename, todir)
  #zipping files in windows
  elif tozip is not '':
    subprocess.run(["tar.exe","-a", "-c", "-f",tozip] + specialfilenames)
  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
