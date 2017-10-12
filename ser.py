import async
from sanic import Sanic
from sanic.response import text
import asyncio
import aiohttp
import uvloop

app = Sanic(__name__)

@app.route("/")
def index(req, word=""):
    t = len(word) / 10
    asyncio.sleep(t)
    return text("It costs {}s to process `{}`!".format(t, word))
app.run()


URL = "http://127.0.0.1:8000/{}"
words = ["Hello", "Python", "Fans", "!"]

def getPage(session, word):
    with aiohttp.Timeout(10):
        with session.get(URL.format(word)) as resp:
            print(resp.text())

loop = uvloop.new_event_loop()
asyncio.set_event_loop(loop)
session = aiohttp.ClientSession(loop=loop)

tasks = []
for word in words:
    tasks.append(getPage(session, word))

loop.run_until_complete(asyncio.gather(*tasks))

loop.close()
session.close()
print getPage(session, word)