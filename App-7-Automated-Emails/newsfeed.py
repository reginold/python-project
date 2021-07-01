import requests


class NewsFeed:

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "10ee29b41dbb4750a37c45c80c470a02"

    def __init__(self, keyword, start_time, to_time) -> None:
        self.keyword = keyword
        self.start_time = start_time
        self.to_time = to_time

    def get(self):
        content = self._get_all_articles()

        email_content = self._email_content(content)

        return email_content

    def _email_content(self, content):
        email_content = ""
        for article in content:
            email_content = (
                email_content + article["title"] + "\n" + article["url"] + "\n"
            )

        return email_content

    def _get_all_articles(self):
        articles = requests.get(
            f"{self.base_url}q={self.keyword}&from={self.start_time}&to={self.to_time}&sortBy=popularity&apiKey={self.api_key}"
        )
        content = articles.json()["articles"]
        return content


if __name__ == "__main__":
    a = NewsFeed(
        keyword="apple",
        start_time="2021-05-30",
        to_time="2021-05-31",
    )
    print(a.get())
