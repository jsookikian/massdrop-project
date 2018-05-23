
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

JOB_STATUS = {
'NEW': "New",
'IN_PROGRESS' : "In Progress",
'DONE' : "Done",
'FAILED' : "Failed"
}


class Job(db.Model):
	__tablename__ = 'job'
	id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
	url = db.Column(db.String(50), nullable=False)
	status = db.Column(db.String(20))
	html = db.Column(db.BLOB, nullable=True)

	def __init__(self, url):
		self.url = url
		self.status= JOB_STATUS['NEW']
		self.html = None


	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}


	def update_html(self, html):
		self.html = html
		db.session.commit()

	def update_status(self, status):
		self.status = status
		db.session.commit()


def add_job(url):
	job = Job(url)
	db.session.add(job)
	db.session.commit()
	return job.id


def fetch_by_id(job_id):
	return Job.query.get(job_id)

