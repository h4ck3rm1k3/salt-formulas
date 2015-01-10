lint:
	python checkpython.py

lintrc:
	~/.local/bin/pylint --generate-rcfile > pylint.rc

