from aiohttp import web

async def health_check(request):
    return web.Response(text="Bot is running!")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", health_check)  # Endpoint utama

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8000)  # Koyeb butuh port 8000
    await site.start()
    print("Web server berjalan di port 8000")
