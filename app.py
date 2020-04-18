from sanic import Sanic
from sanic import response
import aiohttp
import asyncio
import re
from sanic.response import json

app = Sanic(__name__)

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8006)
