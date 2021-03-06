[![Travis Build Status](https://travis-ci.org/0PEIN0/drf-logger.svg?branch=develop)](https://travis-ci.org/0PEIN0/drf-logger)

# drf-logger
Django rest framework logger project.

### Heroku tool-belt install command on ubuntu:
```bash
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```

### Heroku login command:
```bash
heroku login
```

### Heroku configs:

```bash
heroku config:set DISABLE_COLLECTSTATIC=1 --app drf-logger
```
(here `drf-logger` is the heroku-app name)

```bash
heroku config:set HEROKU_ENV=True --app drf-logger
```
(here `drf-logger` is the heroku-app name)

```bash
heroku config:set HEROKU_HOST="drf-logger.herokuapp.com" --app drf-logger
```
(here `drf-logger` is the heroku-app name)

```bash
heroku config:set ADMIN_USER_EMAIL="sample@domain.ext" --app drf-logger
```
(here `drf-logger` is the heroku-app name)

```bash
heroku config:set ADMIN_USER_PASSWORD="django-admin-user-password" --app drf-logger
```
(here `drf-logger` is the heroku-app name)

### Heroku remote container login:

```bash
heroku run bash --app drf-logger
```
(here `drf-logger` is the heroku-app name)
