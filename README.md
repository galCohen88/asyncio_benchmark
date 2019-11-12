# Benchmark async vs sync API

## How?

1. httpaio framework reading / writing values to redis
2. flask framework  reading / writing values to redis

## set up
start redis locally using docker 

$ docker run -p 6379:6379 --name redis -d redis

start locust on each process (sync on 8080 sync on 8081)

$ locust -f http_load.py --host=http://localhost:8080

$ locust -f http_load.py --host=http://localhost:8081

Number of users: the number of users testing your application. Each user opens a TCP connection to your application and tests it.
Hatch rate: For each second, how many users will be added to the current users until the total amount of users. Each hatch Locust calls the on_start function if you have.

## Conclusion
For low rate (10 users), there is no such big difference in performance
For high rate (100 users), its starts getting interesting, where a big difference in response time can be seen 


## Graphic results

### sync 10 clients 10 hatch rate 
![Alt text](10_10_sync.png?raw=true) 

### async 10 clients 10 hatch rate 
![Alt text](10_10_async.png?raw=true) 

### sync 100 clients 100 hatch rate 
![Alt text](100_100_sync.png?raw=true) 

### async 100 clients 100 hatch rate
![Alt text](100_100_async.png?raw=true)

### sync 1000 clients 1000 hatch rate
![Alt text](1000_1000_sync.png?raw=true) 

### async 1000 clients 1000 hatch rate
![Alt text](1000_1000_async.png?raw=true) 