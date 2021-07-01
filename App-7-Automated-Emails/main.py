import datetime
import time

import pandas as pd
import yagmail

from newsfeed import NewsFeed


def send_email(value):
    to_date = datetime.datetime.now().strftime("%Y-%m-%d")
    from_date = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(
        "%Y-%m-%d"
    )

    content = NewsFeed(
        keyword=value["interest"],
        start_time=from_date,
        to_time=to_date,
    )
    email = yagmail.SMTP(user="reggielu03@gmail.com", password="Wobufangqi123")
    email.send(
        to=value["email"],
        subject="Hi there",
        contents=f"hi , this is the content you want!\n{content.get()}",
    )


while True:
    if datetime.datetime.now().hour == 21 and datetime.datetime.now().minute == 21:
        df = pd.read_csv("./people.csv")
        for key, value in df.iterrows():
            send_email(value)

    time.sleep(60)
