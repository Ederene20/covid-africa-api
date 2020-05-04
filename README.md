# Covid-Africa API

## Requirements

- Python 3.4 +
- OpenSSL (latest version)
- Pip
- Masonite
- Masonite-api
- virtualenv

## Setup

```bash
craft install
craft run serve
```

If you are stuck here, refer to this [article](https://www.hellomasonite.com/post/setting-up-a-masonite-development-environment/) to better understand how to setup your masonite development environment.

## Run the project locally

First, configure your database environment. Refer to the official [documentation](https://docs.masoniteproject.com/orator-orm/database-migrations).

```
craft migrate
craft schedule:run --task CreateAfricaData
craft schedule:run --task CreateCountryData
```

Theses tasks will insert the data in your database. The next step now is to update your database. Check [here](https://github.com/Covid-Africa/covid-africa-api/blob/master/app/tasks/README.md) to see how to do it.

## How to use the API :

### GET Country

Return the name of the country, the number of cases, death and recovered.

```
http://covidafrica-api.herokuapp.com/api/africa/countries/:country
```

#### Example

```bash
curl --request GET 'https://covidafrica-api.herokuapp.com/api/africa/countries/Benin'
```

### GET countries

Return the list of every african Country with name, and case, death and recovered numbers.

```
http://covidafrica-api.herokuapp.com/api/africa/countries
```

#### Example

```bash
curl --request GET 'https://covidafrica-api.herokuapp.com/api/africa/countries'
```

### GET historical Africa

Return a list of object containing the date (since 2019-12-31) with the number of cases and deaths; and the new case and new deaths of that day.

```
http://covidafrica-api.herokuapp.com/api/africa/
```

#### Example

```bash
curl --request GET 'https://covidafrica-api.herokuapp.com/api/africa/'
```

### GET Date Africa

Return the number of cases, new cases, deaths and new deaths of the requested date.
Be sure the date is between 2019-12-31 and yesterday date.

```
http://covidafrica-api.herokuapp.com/api/africa/dates/:YYYY-MM-DD
```

#### Example

```bash
curl --request GET 'https://covidafrica-api.herokuapp.com/api/africa/date/2020-01-30'
```

## Maintainers

- [shadowcompiler](https://github.com/shadowcompiler)
- [kolawolemangabo](https://github.com/Kolawole39)

## Contribution

If you're new to contributing to Open Source on Github, this [guide](https://opensource.guide/how-to-contribute/) can help you get started. Please check out the [contribution guide](https://github.com/Covid-Africa/covid-africa-api/CONTRIBUTING.md) for more details on how issues and pull requests work.
