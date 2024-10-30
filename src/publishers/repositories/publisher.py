import os
from airtable import airtable
from dotenv import load_dotenv
from src.publishers.dtos.publisher import PublisherDTO

load_dotenv()

airtable_database_id= os.getenv("AIRTABLE_BASE_ID")
airtable_token = os.getenv("AIRTABLE_TOKEN")

class PublisherRepository:
    def __init__(self):
        self.table = "publishers"
        self.airtable = airtable.Airtable(airtable_database_id, airtable_token)
        self.airtable.create()
    
    def get_publishers(self):
        publisher_records = self.airtable.get(table_name=self.table)
        publishers = []
        for record in publisher_records["records"]:
            fields = record.get('fields')
            publisher = PublisherDTO(
                website=fields['Website'],
                company_selector=fields['Company Selector'],
                date_selector=fields['Date Selector'],
                link_selector=fields['Link Selector'],
                place_selector=fields['Place Selector'],
                scrapping_url=fields['Scrapping URL'],
                title_selector=fields['Title Selector']
            )
            publishers.append(publisher)
        
        return publishers