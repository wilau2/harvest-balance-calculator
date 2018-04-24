[![CircleCI](https://img.shields.io/circleci/project/github/wilau2/harvest-balance-calculator/master.svg)](https://circleci.com/gh/wilau2/harvest-balance-calculator)
[![codecov](https://img.shields.io/codecov/c/github/wilau2/harvest-balance-calculator/master.svg)](https://codecov.io/gh/wilau2/harvest-balance-calculator)
[![tidelift](https://tidelift.com/badges/github/wilau2/harvest-balance-calculator)](https://tidelift.com/repo/github/wilau2/harvest-balance-calculator)
[![](https://images.microbadger.com/badges/image/williamlauze/harvest-balance-calculator.svg)](https://microbadger.com/images/williamlauze/harvest-balance-calculator "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/williamlauze/harvest-balance-calculator.svg)](https://microbadger.com/images/williamlauze/harvest-balance-calculator "Get your own version badge on microbadger.com")

# harvest-balance-calculator
Calculate how much overtime or time you owe based on the average hours you should work per weeks.

## Run

```
docker run --env-file ./env.secret williamlauze/harvest-balance-calculator:latest
```

## Setup
create `env.secret` file containing the following information

```
HARVEST_ACCOUNT_ID=
HARVEST_AUTHORIZATION=
BEGIN_DATE='2016-5-2'
END_DATE='2017-11-24'
HOURS_PER_WORK_DAY=7.5
WORK_DAYS_OF_THE_WEEK=0 1 2 3 4
```



## Github

click [here](https://github.com/wilau2/harvest-balance-calculator/)

## Dockerhub

click [here](https://hub.docker.com/r/williamlauze/harvest-balance-calculator/)

## Timezone
Don't worry !
Harvest will return every time already converted with your timezone
you can make sure your user has the good timezone ->  `GET https://api.harvestapp.com/v2/users/me`

## Beer
If you like this project and want to help. You can buy me a beer [here](https://www.paypal.me/williamlauze)
