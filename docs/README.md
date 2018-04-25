[![CircleCI](https://img.shields.io/circleci/project/github/wilau2/harvest-balance-calculator/master.svg)](https://circleci.com/gh/wilau2/harvest-balance-calculator)
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors)
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

## Contributors

Thanks goes to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
| [<img src="https://avatars0.githubusercontent.com/u/5473183?v=4" width="100px;"/><br /><sub><b>William Lauzé</b></sub>](https://github.com/wilau2)<br />[💻](https://github.com/wilau2/harvest-balance-calculator/commits?author=wilau2 "Code") [📖](https://github.com/wilau2/harvest-balance-calculator/commits?author=wilau2 "Documentation") [🚇](#infra-wilau2 "Infrastructure (Hosting, Build-Tools, etc)") [⚠️](https://github.com/wilau2/harvest-balance-calculator/commits?author=wilau2 "Tests") | [<img src="https://avatars3.githubusercontent.com/u/10335220?v=4" width="100px;"/><br /><sub><b>Boris Fortin Côté</b></sub>](https://github.com/Carkib)<br />[💻](https://github.com/wilau2/harvest-balance-calculator/commits?author=Carkib "Code") |
| :---: | :---: |
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind welcome!