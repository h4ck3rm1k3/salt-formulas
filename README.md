salt-formulas
=============

a collection of all know salt formulas, in git, via submodules

formulas.txt contains a unique list of repos

Build the list with helpers like this :

    python get.py >> formulas.srt 
    python get2.py >> formulas.srt 
    python get3.py  >> formulas.srt 
    sort -u formulas.srt > formulas.txt

the secrets.py contains the github password in a variable p.

generate the checkout script based on the formulas.txt

    python checkout.py > checkout.sh
    bash -x checkout.sh 

checkers
========
find -name \*.yml > yamlfiles.txt
find -name \*.sls > slsfiles.txt
find -name \*.py > pyfiles.txt


setup
=====

python setup.py install --root=~/experiments/salt-formulas/root/
cp -vr conf/* ~/experiments/salt-formulas/root/etc/salt/
export
PYTHONPATH=/mnt/data/home/mdupont/experiments/salt-formulas/root/usr/local/lib/python2.7/dist-packages/

in the file
~/experiments/salt-formulas/root/usr/local/lib/python2.7/dist-packages/salt/_syspaths.py

   ROOT_DIR = '/home/mdupont/experiments/salt-formulas/root/'

mkdir -p /home/mdupont/experiments/salt-formulas/root/var/cache/salt/minion/extmods/renderers
mkdir -p /home/mdupont/experiments/salt-formulas/root/var/cache/salt/minion/extmods/states
mkdir -p /home/mdupont/experiments/salt-formulas/root/var/cache/salt/minion/extmods/renderers
mkdir -p /home/mdupont/experiments/salt-formulas/root/var/cache/salt/minion/extmods/log_handlers
mkdir -p /home/mdupont/experiments/salt-formulas/root/var/cache/salt/minion/extmods/grains
mkdir -p /home/mdupont/experiments/salt-formulas/root/var/cache/salt/minion/extmods/modules
mkdir -p /home/mdupont/experiments/salt-formulas/root/var/cache/salt/minion/extmods/pillar
mkdir -p /home/mdupont/experiments/salt-formulas/root/var/cache/salt/minion/extmods/modules

Now,
the roots in the file root/etc/salt/master
are generated with checksls.py, but tweaked.

Home
====

http:/github.com/h4ck3rm1k3/salt-formulas
