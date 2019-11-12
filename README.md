# Benchmark writing to redis comparing sync vs async (event loop) API

## set up
start redis locally using docker 

$ docker run -p 6379:6379 --name redis -d redis

start locust on each process (sync on 8080 sync on 8081)

locust -f http_load.py --host=http://localhost:8080

locust -f http_load.py --host=http://localhost:8081

The number of users: the number of users testing your application. Each user opens a TCP connection to your application and tests it.
Hatch rate: For each second, how many users will be added to the current users until the total amount of users. Each hatch Locust calls the on_start function if you have.

## Idiomatic results

### sync 10 clients 10 hatch rate 
![Alt text](10_10_sync.png?raw=true "WIFI shield controlling servo motor by http request")

### async 10 clients 10 hatch rate 
![Alt text](10_10_async.png?raw=true "WIFI shield controlling servo motor by http request")

### sync 100 clients 100 hatch rate 
![Alt text](100_100_sync.png?raw=true "WIFI shield controlling servo motor by http request")

### async 100 clients 100 hatch rate
![Alt text](100_100_async.png?raw=true "WIFI shield controlling servo motor by http request")
