# Load testing in python using Locust
link to blog: https://medium.com/@rico098098/load-testing-with-python-fea13369af43


## Purpose
1. Test load capability of the backend
2. In a terminal, running the `locust + args` command (see below) will start a load test with a defined max number of concurrent user, rate of users spawned per second, etc.

## Pre-requisite
`pip install locust`

## usage
1. Modify the file `backend_loadtest.py` if you want to modify the question or test new endpoints
2. Run `locust -f backend_loadtest.py -u 3 -r 10 -t 3m --html report.html` in your conda terminal 
    1. Add --headless to run headless
    2. -u is the number of max concurrent users
    3. -r is the rate to spawn users per second
    4. -t is the time of the test (e.g. 1h, 1m, 60 (default unit is s))
    5. --html exports the report to HTML

