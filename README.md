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

Home
====

http:/github.com/h4ck3rm1k3/salt-formulas
