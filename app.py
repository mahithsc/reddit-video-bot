import asyncio
from getting_reddit_data import get_reddit_data
from make_movie import make_video_from_data

async def main():
    await get_reddit_data()
    make_video_from_data()

asyncio.get_event_loop().run_until_complete(main())