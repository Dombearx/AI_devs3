black:
	poetry run black .

flake:
	poetry run autoflake --quiet --in-place --recursive --ignore-init-module-imports --remove-unused-variables --remove-all-unused-imports .

isort:
	poetry run isort .

typehint_check:
	poetry run mypy --no-site-packages --ignore-missing-imports --no-strict-optional --explicit-package-bases .

format: flake typehint_check black