# Benchmark async vs sync API

## How?

1. httpaio framework reading / writing values to redis
2. flask framework  reading / writing values to redis

## set up
start redis locally using docker 

$ docker run -p 6379:6379 --name redis -d redis

start locust on each process (sync on 8080 sync on 8081)

$ pip install -r requirements.txt

$ locust -f client/http_load.py --host=http://localhost:8080

$ locust -f client/http_load.py --host=http://localhost:8081

Number of users: the number of users testing your application. Each user opens a TCP connection to your application and tests it.
Hatch rate: For each second, how many users will be added to the current users until the total amount of users. Each hatch Locust calls the on_start function if you have.

## Conclusion
With asyncio the response time was X4 faster in average than sync (~50ms median vs ~250ms median)
No major change when using aioredis

## Graphic results

### sync 100 clients 100 hatch rate 
![Alt text](100_100_sync.png?raw=true) 

### async 100 clients 100 hatch rate 
![Alt text](100_100_async.png?raw=true) 
