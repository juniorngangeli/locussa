class PublisherDTO:
    def __init__(
            self,
            website: str,
            scrapping_url: str,
            title_selector: str,
            link_selector: str,
            date_selector: str,
            place_selector: str,
            company_selector: str,
            description_selector: str
    ):
        self.website = website
        self.scrapping_url = scrapping_url
        self.title_selector = title_selector
        self.link_selector = link_selector
        self.date_selector = date_selector
        self.place_selector = place_selector
        self.company_selector = company_selector
        self.description_selector = description_selector