import requests
from bs4 import BeautifulSoup
from dateutil import parser


from src.publishers.dtos.publisher import PublisherDTO
from src.jobs.dtos.job import JobDTO

class ScrapPublisherWebsite:
    def __init__(self, publisher=PublisherDTO):
        self.publisher = publisher

    def execute(self):
        r = requests.get(self.publisher.scrapping_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        titles = soup.select(selector=self.publisher.title_selector)
        links = soup.select(selector=self.publisher.link_selector)
        companies = soup.select(selector=self.publisher.company_selector)
        places = soup.select(selector=self.publisher.place_selector)
        dates = soup.select(selector=self.publisher.date_selector)

        items_count = len(links)

        jobs = []
        for i in range(0, items_count):
            published_at = parser.parse(timestr=dates[i - 1].get_text()).strftime("%Y-%m-%d")
            job = JobDTO(
                title=titles[i - 1].get_text(),
                company= companies[i - 1].get_text(),
                date=published_at,
                link=links[i - 1].get('href'),
                place=places[i - 1].get_text()
            )

            jobs.append(job)

        return jobs