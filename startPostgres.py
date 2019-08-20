#!/usr/bin/env python
  
#enter command ---- chmod a+x filename.py

from subprocess import call

call(["brew","services","start","postgresql"])
