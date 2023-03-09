# Makefile
SHELL = $ENV:SHELL


# Styling
.PHONY: style
style:
	black .
	flake8
	python -m isort .

# Environment
.ONESHELL:
.PHONY: venv
venv:
	conda create -n wheat-yield-prediction-toolkit python=3.9
	conda activate wheat-yield-prediction-toolkit
	python -m pip install pip setuptools wheel
	python -m pip install -e .

# Activation :
.ONESHELL:
.PHONY: activate
activate:
	conda activate wheat-yield-prediction-toolkit

# Cleaning
.PHONY: clean
clean: style
	powershell -Command "Get-ChildItem -Path . -Include *.DS_Store -Recurse -Force | Remove-Item -Force"
	powershell -Command "Get-ChildItem -Path . -Include __pycache__,*.pyc,*.pyo -Recurse -Force | Remove-Item -Force -Recurse"
	powershell -Command "Get-ChildItem -Path . -Include .pytest_cache -Recurse -Force | Remove-Item -Force -Recurse"
	powershell -Command "Get-ChildItem -Path . -Include .ipynb_checkpoints -Recurse -Force | Remove-Item -Force -Recurse"
	powershell -Command "Get-ChildItem -Path . -Include .trash -Recurse -Force | Remove-Item -Force -Recurse"


# Help
.PHONY: help
help:
	@echo "Commands:"
	@echo "venv    : creates a virtual environment."
	@echo "activate	: activates the wheat-yield-prediction-toolkit venv"
	@echo "style   : executes style formatting."
	@echo "clean   : cleans all unnecessary files."

