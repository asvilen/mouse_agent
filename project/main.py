import asyncio
from aiohttp import web

from code.handlers import websocket_handler, http_handler, image_handler


async def main():
    loop = asyncio.get_event_loop()

    app = web.Application()
    app.router.add_get('/ws', websocket_handler)
    app.router.add_get('/', http_handler)
    app.router.add_get('/images/{filename}', image_handler)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

    await asyncio.Event().wait()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
