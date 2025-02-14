from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup

API_ID = '20056432'
API_HASH = '522b74fc06cec9bcbfb7d88d07bad8ff'
BOT_TOKEN = '7333214300:AAH0f9sGxPm5ahEhl80Fbd8UXyZ-uT0l4-Y'
CHANNEL_ID = '-1002253202981'

MOVIE_SITE = "https://popcinemax.blogspot.com"

client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

def get_latest_movie():
    response = requests.get(MOVIE_SITE)
    soup = BeautifulSoup(response.text, 'html.parser')
    movie = soup.find('div', class_='movie-item')  
    title = movie.find('h2').text
    link = movie.find('a')['href']
    return f"🎬 নতুন মুভি: {title}\n🔗 ডাউনলোড: {MOVIE_SITE}{link}"

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("🚀 বট চালু! মুভির লিংক পোস্ট হবে।")

async def post_movie():
    movie_info = get_latest_movie()
    await client.send_message(CHANNEL_ID, movie_info)

with client:
    client.loop.run_until_complete(post_movie())
