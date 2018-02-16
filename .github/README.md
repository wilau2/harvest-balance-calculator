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
    "hoursPerWorkDay": "7.5",
    "workDaysOfTheWeek": [0, 1, 2, 3, 4]
}
```
- workDaysOfTheWeek where 0 is monday

## Run 
### Docker
Each time you change your configuration files, you have to build the docker image with the following command.
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


## Synchronizing commit description with harvest tasks

First, you need to configure what you want to track
most people have open source projects contribution they want to exclude from this
This will select the organization and the repositories you want to track on github

```
pipenv run python configuration.py
```

Afterwards, you want to map each repository to an harvest client

```
pipenv run python configuration2.py
```
if you take a look at your configuration.json.secret the following information will be added
```
"links": [
    {
      "repository": 81864385,
      "project": 12990453
    },
    {
      "repository": 101913270,
      "project": 12990453
    }
]
```



## Timezone
Don't worry! Harvest will return every time already converted with your timezone
you can make sure your user has the good timezone ->  `GET https://api.harvestapp.com/v2/users/me`

## Beer
If you like this project and want to help. You can buy me a beer [here](https://www.paypal.me/williamlauze)
