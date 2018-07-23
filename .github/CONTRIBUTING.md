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

## Add yourself as a contributor

This project follows the [all contributors][all-contributors] specification. To add yourself to the table of
contributors on the README.md, please use the automated script as part of your PR:

```console
npm run contributors:add -- <YOUR_GITHUB_USERNAME>
```

Follow the prompt. If you've already added yourself to the list and are making a new type of contribution, you can run
it again and select the added contribution type.
