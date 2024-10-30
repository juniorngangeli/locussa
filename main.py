from src.publishers.repositories.publisher import PublisherRepository
from src.publishers.actions.scrap_publisher_website import ScrapPublisherWebsite

def main():
    repository = PublisherRepository()
    publishers = repository.get_publishers()
    for publisher in publishers:
        scrapper = ScrapPublisherWebsite(publisher)
        jobs = scrapper.execute()
    

if __name__ == "__main__":
    main()