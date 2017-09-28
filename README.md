# firefox-headless-selenium-python

Create container:
```sh
docker run -p 4444:4444 -p 5900 -d . --name firefox-headless-selenium-python
docker exec firefox-headless-selenium-python bash
```

With docker compose:
```sh
docker-compose exec selenium python3 /app/scripts/example_test.py
vinagre localhost:5900 # pass 'secret'
```

## Referencias
- https://intoli.com/blog/running-selenium-with-headless-firefox/
- https://github.com/SeleniumHQ/docker-selenium/tree/master/StandaloneFirefox
- https://github.com/vvo/docker-selenium-firefox-chrome-beta
