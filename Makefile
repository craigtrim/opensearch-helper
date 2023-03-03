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

linters:
	poetry run pre-commit run --all-files
	poetry run flakeheaven lint

freeze:
	poetry run pip freeze > requirements.txt
	poetry run python -m pip install --upgrade pip

all:
	make linters
	make build
	make freeze
