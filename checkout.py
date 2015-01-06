f = open('formulas.txt')
for l in f.readlines() :
    l=l.rstrip()
    name = l.replace("/","_")
    cmd = "git submodule add https://github.com/%s.git %s" % (l, name)
    print cmd
