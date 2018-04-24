# Contributing

When contributing to this repository, please first discuss the change you wish to make via issues.

Please note we have a code of conduct, please follow it in all your interactions with the project.

All contributions are welcome!


## Pull request process

Read and follow according template


## Issues process

Read and follow according template


## Run

Read and follow `package.json`

## Python
Make sure python3 is installed

### Setup
pip3 install pipenv
cd src
pipenv check
pipenv install
pipenv shell

### Run tests
pipenv run python -m unittest discover -v

### Run application
make sure env.secret is copied in src folder
pipenv run python main.py

### Run coverage
pipenv run coverage run -m unittest discover -v
pipenv run coverage report

## commitizen + cz-conventional-changelog

https://github.com/commitizen/cz-cli