import urllib.request
from server import app, db, Job, celery
from celery.task import task
@celery.task(name='fetch_html', bind=True, max_retries=10)
def fetch_html(self, job_id):
    with app.app_context():
        job_obj = Job.query.get(job_id)
        try:
            req = urllib.request.urlopen(job_obj.url)
            content = req.read()
            # Convert html from binary to string
            job_obj.html = content
            # Change status
            job_obj.status = "done"
            db.session.commit()
        except Exception as exc:
            job_obj.status = "failed: " + str(exc)
            # print("Retrying " + str(self.request.retries) + " number of times")
            db.session.commit()


