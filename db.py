from server import db


class Job(db.Model):
	__tablename__ = 'job'
	id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
	url = db.Column(db.String(50), nullable=False)
	status = db.Column(db.String(20))
	html = db.Column(db.BLOB, nullable=True)

	def __init__(self, url):
		self.url = url
		self.status= 'working'
		self.html = None


	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

