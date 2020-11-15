#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  list_of_puzzle_urls = []
  match = re.search("\w_(\S+)", filename)
  urlstart = "http://" + match.group(1)
  fileread = open(filename, 'r')
  for line in fileread:
    match = re.search("GET (\S+) HTTP",line)
    if "puzzle" in match.group(1):
      url = urlstart + match.group(1)
      if url not in list_of_puzzle_urls:
        list_of_puzzle_urls.append(url)
  
  return sorted(list_of_puzzle_urls)
  # +++your code here+++

def specificFunction(singleUrl):
  print("singleUrl : " + singleUrl)
  match = re.search("/puzzle/(\w+)-(\w+)-(\w+)", singleUrl)
  print("match.group(3) " + match.group(3))
  return match.group(3)

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  #list_of_puzzle_urls = read_urls("animal_code.google.com") 
  list_of_puzzle_urls = read_urls("place_code.google.com")
  list_of_puzzle_urls = sorted(list_of_puzzle_urls,key=specificFunction)
  i = 1
  for url in list_of_puzzle_urls:
    print("Downloading img" + str(i))
    urllib.request.urlretrieve(url, "img" + str(i) + ".jpg")
    i+=1
  htmlimage = open("finalfile.html", 'w')
  htmlimage.write("""<verbatim>"""
                  """<html>"""
                  """<body>""")
  i = 1
  for url in list_of_puzzle_urls:
    htmlimage.write("""<img src=img""" + str(i) + ".jpg" + ">")
    i += 1
  htmlimage.write("</body></html")
  # +++your code here+++
  

def main():
  args = sys.argv[1:]
  read_urls("animal_code.google.com")
  download_images("", "")
  if not args:
    print ('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])
  
  if todir:
    download_images(img_urls, todir)
  else:
    print ('\n'.join(img_urls))

if __name__ == '__main__':
  main()
