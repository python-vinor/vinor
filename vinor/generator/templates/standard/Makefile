env:
	! test -s ./.env && cp ./.env.local.sample ./.env

install:
	pip install -r requirements.txt

start:
	uvicorn standard.main:app --reload

start-sqlite:
	rm .env && cp .env.sqlite .env
	uvicorn standard.main:app --reload

start-mysql:
	rm .env && cp .env.mysql .env
	uvicorn standard.main:app --reload

lint:
	# stop the build if there are Python syntax errors or undefined names
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

test: lint
	pytest

test-feature: lint
	pytest standard/tests/feature

test-unit: lint
	pytest standard/tests/unit

test-mailer: lint
	pytest standard/tests/unit/apps/mailer standard/tests/unit/services/test_mail_service.py



