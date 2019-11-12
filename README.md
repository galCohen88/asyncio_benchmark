start redis locally using docker 

$ docker run -p 6379:6379 --name redis -d redis

start locust on each process (sync on 8080 sync on 8081)

locust -f http_load.py --host=http://localhost:8080

locust -f http_load.py --host=http://localhost:8081

