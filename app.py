import asyncio
from pyppeteer import launch
from gtts import gTTS

async def main():
    browser = await launch(headless = False)
    page = await browser.newPage()
    await page.goto('https://www.reddit.com/r/AskReddit/comments/zd6pxv/whats_something_we_all_just_pretend_no_one_does/')
    
    # downloading the title post
    await page.waitForSelector('#t3_zd6pxv')
    title = await page.querySelector('#t3_zd6pxv')
    await title.screenshot({'path': './video_assets/title.png'})

    # getting the title of the post
    element = await page.querySelector('#t3_zd6pxv > div > div._2FCtq-QzlfuN-SwVMUZMM3._2v9pwVh0VUYrmhoMv1tHPm.t3_zd6pxv > div.y8HYJ-y_lTUHkQIc1mdCq._2INHSNB8V5eaWp4P0rY_mE > div > h1')
    title = await page.evaluate('(element) => element.textContent', element)

    # downloading comment screenshot
    await page.waitForSelector('#t1_iz18nn8 > div.Comment.t1_iz18nn8.P8SGAKMtRxNwlmLz1zdJu.HZ-cv9q391bm8s7qT54B3._1z5rdmX8TDr6mqwNv7A70U')
    comment = await page.querySelector('#t1_iz18nn8 > div.Comment.t1_iz18nn8.P8SGAKMtRxNwlmLz1zdJu.HZ-cv9q391bm8s7qT54B3._1z5rdmX8TDr6mqwNv7A70U')
    await comment.screenshot({'path': './video_assets/comment.png'})

    # getting text content of the comment
    await page.waitForSelector('#t1_iz18nn8 > div.Comment.t1_iz18nn8.P8SGAKMtRxNwlmLz1zdJu.HZ-cv9q391bm8s7qT54B3._1z5rdmX8TDr6mqwNv7A70U')
    commentTextAtr = await page.querySelector('#t1_iz18nn8 > div.Comment.t1_iz18nn8.P8SGAKMtRxNwlmLz1zdJu.HZ-cv9q391bm8s7qT54B3._1z5rdmX8TDr6mqwNv7A70U > div._3tw__eCCe7j-epNCKGXUKk > div._3cjCphgls6DH-irkVaA0GM > div')
    commentText = await page.evaluate('(commentTextAtr) => commentTextAtr.textContent', commentTextAtr)

    # convertingt o mp3 files
    gTTS(text=title, lang='en', slow=False).save('./video_assets/titleTTS.mp3')
    gTTS(text=commentText, lang='en', slow=False).save('./video_assets/commentTTS.mp3')


    jsonData = {
        "title": title,
        "comment": commentText
    }

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())