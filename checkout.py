
import os
import os.path

import github3
import urllib2
from secret import p
gh = github3.login('h4ck3rm1k3', password=p)
import re

repos = {}
f = open('.gitmodules')
for l in f.readlines() :
    l=l.rstrip()
    m = re.search('github\.com\/([\w\d\-]+)\/([\w\d\-]+)\.git', l)

    if m:
        l = "%s/%s"  % m.groups()
        print l
        repos[l]=1
f.close()

skip = [
    'damiencaselli_salt-web'
]

keys = ("saltstack",
        "salt stack",
        "salt state",
        "salt formula",
)

for k in keys:
    for r in gh.search_repositories(k, sort='forks'):
        n = str(r.repository)
        if n not in repos :

            print "found new",n
            repos[n]=1

for l in repos.keys():
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
