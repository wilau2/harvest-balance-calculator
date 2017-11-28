# harvest-balance-calculator

With this project you can calculate how much overtime or time you owe based on the average hours you should work per weeks.

## Harvest credentials
[wiki](https://github.com/wilau2/harvest-balance-calculator/wiki/Setting-up-harvest-credentials)

## Usage

`config.json`
```json
{
    "beginDate": "2016-5-2",
    "endDate": "2017-11-24",
    "hoursPerWorkWeek": "37.5",
    "hoursPerWorkDay": "7.5",
    "workDaysOfTheWeek": [0, 1, 2, 3, 4]
}
```
*workDaysOfTheWeek where 0 is monday

## Run 
### Docker
- `docker build -t harvest-balance-calculator .`
- `docker run harvest-balance-calculator`

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
