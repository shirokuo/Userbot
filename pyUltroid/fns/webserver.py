import asyncio
from aiohttp import web

async def health_check(request):
    """Endpoint utama untuk mengecek apakah bot berjalan"""
    return web.Response(text="Bot is running!")

async def start_web_server():
    """Memulai server web menggunakan aiohttp"""
    app = web.Application()
    app.router.add_get("/", health_check)  # Tambahkan endpoint utama

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8000)  # Koyeb/VPS memerlukan port 8000
    await site.start()
    print("✅ Web server berjalan di port 8000")

    # Gunakan asyncio.Event() untuk menjaga server tetap berjalan
    stop_event = asyncio.Event()
    await stop_event.wait()

if __name__ == "__main__":
    asyncio.run(start_web_server())  # Menjalankan web server secara mandiri jika dieksekusi langsung
