# harvest
## credentials
- Login to [harvest](https://id.getharvest.com/developers)
- ![alt text](https://raw.githubusercontent.com/wilau2/harvest-balance-calculator/master/.github/harvest_creds_creation_step1.png)
- ![alt text](https://raw.githubusercontent.com/wilau2/harvest-balance-calculator/master/.github/harvest_creds_creation_step2.png)
- ![alt text](https://raw.githubusercontent.com/wilau2/harvest-balance-calculator/master/.github/harvest_creds_creation_step3.png)
- Add to following section to your `env.secret`

```
HARVEST_ACCOUNT_ID=123456
HARVEST_AUTHORIZATION=Bearer 65776576576675765765
```

## Timezone
Don't worry !
Harvest will return every time already converted with your timezone
you can make sure your user has the good timezone ->  `GET https://api.harvestapp.com/v2/users/me`