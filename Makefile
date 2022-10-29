# Recursively removes all .pyc files and __pycache__ directories in the current directory
clean:
	@find . | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf
	@echo "Removed all pyc files and __pycache__ directories"

lint:
	# stop the build if there are Python syntax errors or undefined names
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

test: lint
	pytest
