from aiohttp import web


async def handler(request):
    return web.Response(text='<h1>Hello world AIO!!!</h1>')

app = web.Application()
app.add_routes([web.get('/', handler)])
y

web.run_app(app, host='localhost', port=3001)
