#!/usr/bin/env python    

#enter command ---- chmod a+x filename.py

from subprocess import call

call(["brew","services","stop","postgresql"])
call(["rm","/usr/local/var/postgres/postmaster.pid"])
call(["brew","services","start","postgresql"])
