import yaml
import sys
from jinja2 import Environment, PackageLoader, Template

def check(fn):
    #print fn
    f = open (fn)
    data = ""
    c = 0
    firstline = ""
    for x in f.readlines():
        if c == 0 :
            #print x
            firstline = x
        c = c + 1
        data = data + x

    try:
        yaml.load(data)
        #print 'OK', fn
    except Exception as e :
        #print 'YAML FAILED', fn

        try :
            eval(data)
            #print 'PYOK', fn
        except Exception as e2 :
            #print "Python failed:",e2
        
            try :
                t = Template(data)
                #print "template OK"
                #print t
                
            except Exception as e3 :
                print fn
                print "template failed:",e3
                #print data
            
        
        pass
        

for l in ['yamlfiles.txt','slsfiles.txt']:
    print l
    f = open (l)
    for x in f.readlines():
        check(x.rstrip())
    

