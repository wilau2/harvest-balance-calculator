# Harvest balance calculator
[![circleci][circleci-badge]][circleci]
[![codecov][codecov-badge]][codecov]
[![tidelift][tidelift-badge]][tidelift]

[![docker image][microbadger-image-badge]][microbadger]
[![docker version][microbadger-version-badge]][microbadger]
[![Docker Pulls][docker-pulls-badge]][docker]

[![donate][donate-badge]][donate]
[![license][license-badge]][license]
[![all contributors][all-contributors-badge]][all-contributors]

[![GitHub Stars][github-stars-badge]][github]

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
| [<img src="https://avatars0.githubusercontent.com/u/5473183?v=4" width="100px;"/><br /><sub><b>William Lauzé</b></sub>](https://github.com/wilau2)<br />[💻](https://github.com/wilau2/harvest-balance-calculator/commits?author=wilau2 "Code") [📖](https://github.com/wilau2/harvest-balance-calculator/commits?author=wilau2 "Documentation") [🚇](#infra-wilau2 "Infrastructure (Hosting, Build-Tools, etc)") [⚠️](https://github.com/wilau2/harvest-balance-calculator/commits?author=wilau2 "Tests") | [<img src="https://avatars3.githubusercontent.com/u/10335220?v=4" width="100px;"/><br /><sub><b>Boris Fortin Côté</b></sub>](https://github.com/Carkib)<br />[💻](https://github.com/wilau2/harvest-balance-calculator/commits?author=Carkib "Code") | [<img src="https://avatars3.githubusercontent.com/u/28273478?v=4" width="100px;"/><br /><sub><b>Karine Larouche</b></sub>](https://github.com/karine-larouche)<br />[💻](https://github.com/wilau2/harvest-balance-calculator/commits?author=karine-larouche "Code") [📖](https://github.com/wilau2/harvest-balance-calculator/commits?author=karine-larouche "Documentation") [⚠️](https://github.com/wilau2/harvest-balance-calculator/commits?author=karine-larouche "Tests") | [<img src="https://avatars2.githubusercontent.com/u/26336230?v=4" width="100px;"/><br /><sub><b>etienne-m</b></sub>](https://github.com/Etienne-M)<br />[💻](https://github.com/wilau2/harvest-balance-calculator/commits?author=Etienne-M "Code") |
| :---: | :---: | :---: | :---: |
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind welcome!

## License

MIT

[circleci-badge]: https://img.shields.io/circleci/project/github/wilau2/harvest-balance-calculator/master.svg
[circleci]: https://circleci.com/gh/wilau2/harvest-balance-calculator
[all-contributors-badge]: https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square
[all-contributors]: #contributors
[codecov-badge]: https://img.shields.io/codecov/c/github/wilau2/harvest-balance-calculator/master.svg
[codecov]: https://codecov.io/gh/wilau2/harvest-balance-calculator
[tidelift-badge]: https://tidelift.com/badges/github/wilau2/harvest-balance-calculator
[tidelift]: https://tidelift.com/repo/github/wilau2/harvest-balance-calculator
[donate-badge]: https://img.shields.io/badge/$-support-green.svg?style=flat-square
[donate]: https://www.paypal.me/williamlauze/10
[license-badge]: https://img.shields.io/github/license/mashape/apistatus.svg
[license]: https://github.com/wilau2/harvest-balance-calculator/blob/master/LICENSE
[microbadger-image-badge]: https://images.microbadger.com/badges/image/williamlauze/harvest-balance-calculator.svg
[microbadger-version-badge]: https://images.microbadger.com/badges/version/williamlauze/harvest-balance-calculator.svg
[microbadger]: https://microbadger.com/images/williamlauze/harvest-balance-calculator
[docker-pulls-badge]: https://img.shields.io/docker/pulls/williamlauze/harvest-balance-calculator.svg
[docker]: https://hub.docker.com/r/williamlauze/harvest-balance-calculator
[github-stars-badge]: https://img.shields.io/github/stars/wilau2/harvest-balance-calculator.svg?style=social&label=Stars
[github]: https://github.com/wilau2/harvest-balance-calculator
