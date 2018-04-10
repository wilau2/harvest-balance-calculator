[![CircleCI](https://circleci.com/gh/wilau2/harvest-balance-calculator.svg?style=svg)](https://circleci.com/gh/wilau2/harvest-balance-calculator)

# harvest-balance-calculator

With this project you can calculate how much overtime or time you owe based on the average hours you should work per weeks.

## Harvest credentials
[wiki](https://github.com/wilau2/harvest-balance-calculator/wiki/Setting-up-harvest-credentials)

## Usage
`env.secret`
```
HARVEST_ACCOUNT_ID=
HARVEST_AUTHORIZATION=
BEGIN_DATE='2016-5-2'
END_DATE='2017-11-24'
HOURS_PER_WORK_DAY=7.5
WORK_DAYS_OF_THE_WEEK=0 1 2 3 4
```
- workDaysOfTheWeek where 0 is monday

## Run 
### Docker
Each time you change your configuration files, you have to build the docker image with the following command.
- `docker build -t harvest-balance-calculator .`
- `docker run harvest-balance-calculator`

get latest version on dockerhub.com
- `docker run -v $(pwd)/config.json.secret:/www/config.json.secret harvest-balance-calculator`
- `docker run --env-file ./env.secret harvest-balance-calculator`

### Python
- Make sure python3 is installed.
- `pip3 install pipenv`
- `pipenv check`
- `pipenv install`
- `pipenv shell`
- `pipenv run python main.py`

## Tests
### Docker
- `docker run harvest-balance-calculator python3 -m unittest discover -v`
### Python
- `pipenv run python -m unittest discover -v`

## Timezone
Don't worry !
Harvest will return every time already converted with your timezone
you can make sure your user has the good timezone ->  `GET https://api.harvestapp.com/v2/users/me`

## Beer
If you like this project and want to help. You can buy me a beer [here](https://www.paypal.me/williamlauze)
