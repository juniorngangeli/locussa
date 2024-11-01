class JobDTO:
    def __init__(self, title: str, link: str, date: str, place: str, company: str, description: str):
        self.title = title
        self.link = link
        self.date = date
        self.place = place
        self.company = company
        self.description = description
    
    def to_dict(self):
        return {
            "title": self.title,
            "link": self.link,
            "date": self.date,
            "place": self.place,
            "company": self.company,
            "description": self.description,
        }