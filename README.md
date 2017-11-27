# harvest-balance-calculator

With this project you can calculate how much overtime or time you owe based on the average hours you should work per weeks.

## Harvest credentials
[wiki](https://github.com/wilau2/harvest-balance-calculator/wiki/Setting-up-harvest-credentials)

## Usage

Make sure to use beginDate and endDate where you have worked full weeks.
`config.json`

```json
{
    "beginDate": "2016-5-3",
    "endDate": "2017-11-24",
    "hoursPerWeek": "37.5"
}
```

## Run with docker. 
### npm 
- `npm run docker:build`
- `npm run docker:run`
### without npm
- `docker build -t harvest-balance-calculator .`
- `docker run harvest-balance-calculator`

## Run with python

- Make sure python3 is installed.

- `pip3 install pipenv`
- `pipenv check`
- `pipenv install`
- `pipenv run python main.py`

## Run tests
- `pipenv run python -m unittest discover -v`

## Timezone

Don't worry !
Harvest will return every time already converted with your timezone
you can make sure your user has the good timezone ->  `GET https://api.harvestapp.com/v2/users/me`
