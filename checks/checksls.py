import yaml
import sys
from jinja2 import Environment, PackageLoader, Template
import os


def check(fn):
    print("Consider {0}".format(fn))
    r = os.system("~/.local/bin/pylint -E --rcfile=pylint.rc %s" % fn)
    if r not in (0, 512) : # 512= check failed
        raise Exception('fail %s'  % r)
      
seen = {}

print """
file_roots:
  base:
"""


def proc(root):
    # check if all parts of path are not seen
    parts = os.path.split(root)
    #print 'check parts', parts
    np = []
    for p in parts :
        np.append(p)
        x = '/'.join(np)
        if x in seen :
            return False
        else:
            #print "new part ", p, "joined", x,  "newpath",np
            pass

    print """     - """ + os.path.abspath(root)
    seen[root]=root
    #print "ROOT",root 
    for x in dirs :
        d= os.path.join(root,x)
        seen[d]=root
            
    
for root, dirs, files in os.walk("./"):
    for filen in files:
        if filen.endswith(".sls"):
            proc(root)
                    
        

