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
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def zipSpecial(zipname, fromdir):
    cmd = 'zip -j ' + zipname+ ' '
    for specialfile in listSpecial(fromdir):
        cmd += specialfile+" "
    status, output = commands.getstatusoutput(cmd)
    print output

def copySpecial(todir, fromdir):
    if not os.path.exists(todir): os.mkdir(todir)
    for copyfile in listSpecial(fromdir):
      # print os.path.basename(copyfile)
      shutil.copy(copyfile, os.path.join(todir,os.path.basename(copyfile)))

def listSpecial(dir):
    ret = []
    for filename in os.listdir(dir):
        match = re.search(r'\w+__\w+__',filename)
        if match:
            ret.append(os.path.join(os.path.abspath(dir),filename))
    return ret

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    fromdir = args[2]
    copySpecial(todir, fromdir)
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    zipname = args[1]
    fromdir = args[2]
    zipSpecial(zipname, fromdir)
    del args[0:2]

  listSpecial(args[0])
  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
  main()
