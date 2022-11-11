run:
	poetry run python -m service

lint:
	poetry run isort service tests
	poetry run black service tests

req:
	poetry export -f requirements.txt --without-hashes --without dev --output requirements.txt
