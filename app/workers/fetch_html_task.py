import urllib.request

from models.job import JOB_STATUS, fetch_by_id

from app import app
from app import celery


@celery.task(name='fetch_html', bind=True, max_retries=10)
def fetch_html(self, job_id):
    with app.app_context():
        job_obj = fetch_by_id(job_id)
        try:
            req = urllib.request.urlopen(job_obj.url)
            content = req.read()
            # Convert html from binary to string
            job_obj.update_html(content)
            # Change status
            job_obj.update_status(JOB_STATUS['DONE'] )
        except Exception as exc:
            job_obj.update_status(JOB_STATUS['FAILED'] )
            # print("Retrying " + str(self.request.retries) + " number of times")


