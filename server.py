from __future__ import print_function
from flask import Flask, render_template, request, json, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from flask_celery import make_celery

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
celery = make_celery(app)

class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    url = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20))
    html = db.Column(db.UnicodeText(20000000), nullable=True)

    def __init__(self, url):
        self.url = url
        self.status= 'working'
        self.html = None

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def add_job(url):
    job = Job(url)
    db.session.add(job)
    db.session.commit()
    tasks.fetch_html.apply_async(args=[job.id], countdown=0)
    return job.id


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/job/<job_id>", methods=['GET'])
def get_job(job_id):
    try:
        job = Job.query.get(job_id).as_dict()
        if ('html' in request.headers['Accept']) and (job['html'] is not None):
            #trim off the 'b from the byte encoding
            return job['html'], 200
        return jsonify(job)
    except AttributeError as e:
        return render_template('404.htm'),404



#Handle post
@app.route('/newJob', methods=['POST'])
def start_job():
    if len(request.form['url']) > 0:
        urlToFetch = request.form['url']
    else:
        redirect("/")
    # urllib requires 'http://' in order to fetch html, so we need to add it here
    if 'http://' not in urlToFetch:
        urlToFetch = 'http://' + urlToFetch
    job_id = add_job(urlToFetch)

    return redirect(url_for('get_job', job_id=job_id))

import tasks
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
    db.create_all()





