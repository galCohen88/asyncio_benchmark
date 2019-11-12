from aiohttp import web
import redis
r = redis.Redis(host='localhost', port=6379, db=0)


async def set_val(request):
    key = request.match_info.get('key')
    value = request.match_info.get('value')
    result = r.set(key, value)
    return web.Response(text=str(result))


async def get_val(request):
    key = request.match_info.get('key')
    result = r.get(key)
    return web.Response(text=str(result))


app = web.Application()
app.add_routes([web.get('/set/{key}/{value}', set_val),
                web.get('/get/{key}', get_val)])

if __name__ == '__main__':
    web.run_app(app)
