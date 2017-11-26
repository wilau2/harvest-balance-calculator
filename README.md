# harvest-balance-calculator

With this project you can calculate how much overtime or time you owe based on the average hours you should work per weeks.

# setup

- Make sure python3 is installed.

- `pip3 install pipenv`

- `pipenv install`

## Credentials

- Login to harvest

- Go to `https://id.getharvest.com/developers`

![alt text](https://github.com/wilau2/harvest-balance-calculator/blob/master/docs/harvest_creds_creation_step1.png)

![alt text](https://github.com/wilau2/harvest-balance-calculator/blob/master/docs/harvest_creds_creation_step2.png)

![alt text](https://github.com/wilau2/harvest-balance-calculator/blob/master/docs/harvest_creds_creation_step3.png)

- create a `config.json.secret` file at root of project.

```json
{
    "harvest": {
        "accountId":"superSecretAccountId",
        "authorization":"Bearer superSecretBearerAuthorizationToken"
    }
}
```

- verify that the configuration in config.json are good for you.

```json
{
    "beginDate": "2016-5-3",
    "endDate": "2017-11-24",
    "hoursPerWeek": "37.5"
}
```

# Run 

`pipenv run python main.py`

# Timezone

Don't worry !

Harvest will return every time already converted with your timezone

you can make sure your user has the good timezone ->  `GET https://api.harvestapp.com/v2/users/me`