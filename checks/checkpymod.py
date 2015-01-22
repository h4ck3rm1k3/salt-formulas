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


import re

def scanmod(fn):
    #print "scanning fn", fn
    
    fh = open(fn)
    for dl in fh.readlines():
        m = re.search(r'__virtual',dl)
        if m:
            fh.close()
            return True
    fh.close()
    return False

def proc(root, fn):

    if fn.startswith('.#'):
        return False 

    # check if all parts of path are not seen
    parts = os.path.split(root)
    #print 'check parts', parts
    np = []

    if scanmod(os.path.join(root,fn)):
        #print "Found a live module in", root
        if root not in  seen:
            #print """    "{0}",""".format( os.path.abspath(root))
            pass
        seen[root]=root
        return True
    return False


def proc2(root, fn):
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

    #print """    "{0}",""".format( os.path.abspath(root))
    seen[root]=root
    #print "ROOT",root 
    for x in dirs :
        d= os.path.join(root,x)
        seen[d]=root
            
    
for root, dirs, files in os.walk("./"):
    for fn in files:
        if fn.endswith(".py"):
            proc(root, fn)
                    
####
mod_list = []
ret_list = []
state_list = []

for x in seen :
    if x.endswith('_states'):
        state_list.append(x)
    elif x.endswith('_returners'):
        ret_list.append(x)
    else:
        mod_list.append(x)

modules = ",\n".join(mod_list)
print """
module_dirs: [ 
{0}
]
""".format(modules)

modules = ",\n".join(ret_list)
print """
returner_dirs: [ 
{0}
]
""".format(modules)

modules = ",\n".join(state_list)
print """
states_dirs: [ 
{0}
]
""".format(modules)
