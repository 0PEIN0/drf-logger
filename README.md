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
