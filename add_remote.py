f = open('formulas.txt')
for l in f.readlines() :
    l=l.rstrip()
    name = l.replace("/","_")
    (owner,repo) = l.split("/")
    cmd = "pushd {0}; git remote add mdupont git@github.com:h4ck3rm1k3/{1}.git; popd".format(name, repo)
    print cmd
