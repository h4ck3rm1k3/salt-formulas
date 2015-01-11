
import os
import os.path

import github3
import urllib2
from secret import p

import re

import sys
skip = [
    'damiencaselli_salt-web'
]


def process(l):
    name = l.replace("/","_")
    cmd =''
    if name not in skip :
        if not os.path.exists(name):
            print 'missing', name
            cmd = "git submodule add --force https://github.com/%s.git %s >> log.txt 2>&1" % (l, name)
            o =  os.system(cmd)
            print "output",o, "command", cmd
            #assert o ==0
        (owner,repo) = l.split("/")
        cmd = "cd {0} && git remote add mdupont git@github.com:h4ck3rm1k3/{1}.git >> log.txt 2>&1".format(name, repo)
        o =  os.system(cmd)
        if o != 32768:
            print o, cmd
            assert o ==0

def readfile(name):
    f = open(name)
    for l in f.readlines() :
        l=l.rstrip()
        process(l)

def search():
    gh = github3.login('h4ck3rm1k3', password=p)
    repos = {}
    f = open('.gitmodules')
    for l in f.readlines() :
        l=l.rstrip()
        m = re.search('github\.com\/([\w\d\-]+)\/([\w\d\-]+)\.git', l)
        if m:
            l = "%s/%s"  % m.groups()
            print ("Process repo %s" % l)
            repos[l]=1
    f.close()

    keys = ("saltstack",
            "salt stack",
            "salt-stack",
            "salt-stack",
            "salt module",
            "salt pillar",
            "salt state",
            'Halite',
            'Salt-Master',
            'Salt-Minion',
            'Salt Master',
            'Salt Minion',
            "salt formula",
            "salt-formula",
            "salt extension:sls language:Scheme",
            "salt extension:sls language:SaltStack",
            'user:saltstack-formulas',
            'user:saltstack')
    for k in keys:
        for r in gh.search_repositories(k, sort='forks'):
            n = str(r.repository)
            if n not in repos :
                print "found new",n
                repos[n]=1
    for l in repos.keys():
        process(l)

def main():
    if sys.argv[1]:
        readfile(sys.argv[1])
    else:
        search()


main()
