lintrc:
	~/.local/bin/pylint --generate-rcfile > pylint.rc

lint:
	python checkpython.py
