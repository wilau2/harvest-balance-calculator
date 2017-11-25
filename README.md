# harvest-balance-calculator

With this project you can calculate how much overtime or time you owe based on the average hours you should work per weeks.

# setup

-Install python3

# Credentials

create a `config.json.secret` file at root of project.

```json
{
    "harvest": {
        "accountId":"superSecretAccountId",
        "authorization":"Bearer superSecretBearerAuthorizationToken"
    }
}
```

verify that the configuration in config.json are good for you.

```json
{
    "hoursPerWeek": "37.5",
}
```

# Timezone

Harvest will return every time already converted with your timezone

to make sure your user has the good timezone `GET https://api.harvestapp.com/v2/users/me`