#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  fileread = open(filename, 'r')
  year = 0
  return_list = []
  list_tuples = []
  for line in fileread:
    if year == 0:
      match = re.search(r'\<h3\salign="center">Popularity\sin\s\w\w\w\w',line)
      if match:
        new_match = re.search(r'\d\d\d\d',match.group())
        year = new_match.group()
        return_list.append(year)
    else:
      match = re.search(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',line)
      if match:
        #print (match.group())
        list_tuples.append((match.group(2), match.group(1)))
        list_tuples.append((match.group(3), match.group(1)))
        #men_dictionary[match.group(1)] = match.group(2)
        #women_dictionary[match.group(1)] = match.group(3)
  list_tuples.sort()
  for tuples in list_tuples:
    appendable = tuples[0] + " " + tuples[1]
    return_list.append(appendable)
  print(return_list)
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  #extract_names("baby1990.html")
  #if not args:
    #print ('usage: [--summaryfile] file [file ...]')
    #sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  #if args[0] == '--summaryfile':
  #  summary = True
  #  del args[0]
  for year in range(1990, 2009, 2):
    extract_names("baby" + str(year) + ".html")
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
