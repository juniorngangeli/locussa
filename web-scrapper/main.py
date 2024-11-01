from src.publishers.repositories.publisher import PublisherRepository
from src.publishers.actions.scrap_publisher_website import ScrapPublisherWebsite
from src.jobs.actions.push_jobs_to_webhook import PushJobsToWebhook

def main():
    repository = PublisherRepository()
    publishers = repository.get_publishers()
    for publisher in publishers:
        scrapper = ScrapPublisherWebsite(publisher)
        jobs = scrapper.execute()
        webhook_pusher = PushJobsToWebhook(jobs)
        webhook_pusher.execute()
    

if __name__ == "__main__":
    main()