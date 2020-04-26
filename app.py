from sanic import Sanic
from sanic import response
import aiohttp
import asyncio
import re
from sanic.response import json
from algoliasearch.search_client import SearchClient

client = SearchClient.create('RM1BDPW8T9', 'e2987be50686f94f846bd36efae9b8c4')
content_idx = client.init_index('Content_production')

app = Sanic(__name__)

@app.route('/')
async def test(request):
    return json({'hello': ['mars', 'jupiter', 'venus']})

@app.route('/analogue/search')
async def get_analogue_content(request):
	return json(content_idx.search(request.args['q']))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8006)
