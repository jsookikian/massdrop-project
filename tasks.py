import urllib
from server import app, db, Job, celery
@celery.task(name='fetch_html', timeout=10, max_retries=3)
def fetch_html(job_id):
    with app.app_context():
        job_obj = Job.query.get(job_id)
        try:
            request = urllib.request.urlopen(job_obj.url)
            content = request.read()
            # Convert html from binary to string
            job_obj.html = content
            # Change status
            job_obj.status = "done"
            db.session.commit()
        except Exception as exc:
            job_obj.status = "failed"
            db.session.commit()
            # self.retry(exc=exc, countdown=2 ** self.request.retries)


