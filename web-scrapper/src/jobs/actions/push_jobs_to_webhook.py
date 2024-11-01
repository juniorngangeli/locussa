import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

from src.jobs.dtos.job import JobDTO
class PushJobsToWebhook:
    def __init__(self, jobs=list[JobDTO]) -> None:
        self.jobs = jobs

    def execute(self):
        jobs_json = json.dumps({"data": [job.to_dict() for job in self.jobs]})
        webhook_url = os.getenv("NEW_JOB_WEBHOOK")
        response = requests.post(
            url=webhook_url,
            data=jobs_json,
            headers={"Content-Type": "application/json"}
        )

        # Check the response
        if response.status_code == 200:
            print("Jobs posted successfully!")
        else:
            print(f"Failed to post jobs. Status code: {response.status_code}")
            print(response.text)
