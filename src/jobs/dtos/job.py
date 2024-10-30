class JobDTO:
    def __init__(self, title: str, link: str, date: str, place: str, company: str):
        self.title = title
        self.link = link
        self.date = date
        self.place = place
        self.company = company
    
    def to_dict(self):
        return {
            "title": self.title,
            "link": self.link,
            "date": self.date,
            "place": self.place,
            "company": self.company
        }