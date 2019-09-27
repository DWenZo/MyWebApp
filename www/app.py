from aiohttp import web

# define server return request "Awesome Website"
# 定义服务器响应请求的的返回为 "Awesome Website"

async def index(request):
    return web.Response(body=b'<h1>Awesome Website</h1>', content_type='text/html')

# establish server app, listen to local 9000
# 建立服务器应用，持续监听本地9000端口的http请求，对首页"/"进行响应

def init():
    app = web.Application()
    app.router.add_get('/', index)
    web.run_app(app, host='127.0.0.1', port=9000)

if __name__ == "__main__":
    init()
