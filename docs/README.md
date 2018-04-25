[![CircleCI](https://img.shields.io/circleci/project/github/wilau2/harvest-balance-calculator/master.svg)](https://circleci.com/gh/wilau2/harvest-balance-calculator)
[![codecov](https://img.shields.io/codecov/c/github/wilau2/harvest-balance-calculator/master.svg)](https://codecov.io/gh/wilau2/harvest-balance-calculator)
[![tidelift](https://tidelift.com/badges/github/wilau2/harvest-balance-calculator)](https://tidelift.com/repo/github/wilau2/harvest-balance-calculator)
[![](https://images.microbadger.com/badges/image/williamlauze/harvest-balance-calculator.svg)](https://microbadger.com/images/williamlauze/harvest-balance-calculator "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/williamlauze/harvest-balance-calculator.svg)](https://microbadger.com/images/williamlauze/harvest-balance-calculator "Get your own version badge on microbadger.com")

# harvest-balance-calculator
Calculate how much overtime or time you owe based on the average hours you should work per weeks.

## Setup
* create `env.secret` file containing the following information

```
HARVEST_ACCOUNT_ID=
HARVEST_AUTHORIZATION=
BEGIN_DATE='2016-5-2'
END_DATE='2017-11-24'
HOURS_PER_WORK_DAY=7.5
WORK_DAYS_OF_THE_WEEK=0 1 2 3 4
```
* get your [harvest credentials](harvest.md)

## Run
* docker
```
docker pull williamlauze/harvest-balance-calculator:latest
docker run --env-file ./env.secret williamlauze/harvest-balance-calculator:latest
```
* npm
```
npm run start
```
