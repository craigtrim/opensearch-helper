# ----------------------------------------------------------------
# helpers/opensearch-helper
# ----------------------------------------------------------------

ifeq ($(OS),Windows_NT)
    os_shell := powershell
	copy_setup := resources/scripts/copy_setup.ps1
else
    os_shell := $(SHELL)
	copy_setup := resources/scripts/copy_setup.sh
endif

copy_setup:
	$(os_shell) $(copy_setup)

# ----------------------------------------------------------------

install:
	poetry check
	poetry lock
	poetry update
	poetry install

test:
	poetry run pytest --disable-pytest-warnings

build:
	make install
	make test
	poetry build
	make copy_setup

integration:
	poetry run python drivers/opensearch_dev_driver.py

mypy:
#	poetry run mypy opensearch_helper
	poetry run stubgen .\opensearch_helper\ -o stubs

linters:
	poetry run pre-commit run --all-files
	poetry run flakeheaven lint

pyc:
	poetry run python -c "import compileall; compileall.compile_dir('opensearch_helper', optimize=2, force=True, legacy=True)"
	poetry run python -c "import compileall; compileall.compile_dir('opensearch_helper', optimize=2, force=True, legacy=False)"

freeze:
	poetry run pip freeze > requirements.txt
	poetry run python -m pip install --upgrade pip

all:
	make build
#	'docker-compose up'	must be running for this to work
#	make integration
	make linters
	make mypy
	make pyc
	make freeze
