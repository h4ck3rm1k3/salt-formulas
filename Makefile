lint:
	python checkpython.py

lintrc:
	~/.local/bin/pylint --generate-rcfile > pylint.rc

all_modules:
	PYTHONPATH=~/experiments/salt:~/experiments/jinja2 python tests/all_modules.py
