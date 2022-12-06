import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless = False)
    page = await browser.newPage()
    await page.goto('https://www.reddit.com/r/AskReddit/comments/zdvqod/what_are_you_addicted_to/')
    await page.waitForSelector('#t3_zdvqod')
    element = await page.querySelector('#t3_zdvqod')
    await element.screenshot({'path': '/video_assets/title.png'})

asyncio.get_event_loop().run_until_complete(main())