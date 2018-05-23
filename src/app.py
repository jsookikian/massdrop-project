from flask import Flask, render_template, request, redirect, jsonify, url_for

from flask_celery import make_celery
from models import job
from utilities import getValidatedUrl

app = Flask(__name__)
app.config.from_pyfile('config.py')
celery = make_celery(app)
job.db.init_app(app)

from workers import fetch_html_task
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/job/<job_id>", methods=['GET'])
def get_job(job_id):
    try:
        job_obj = job.fetch_by_id(job_id).as_dict()
        if ('html' in request.headers['Accept']) and (job_obj['html'] is not None):
            return job_obj['html'], 200
        else:
            job_obj['html'] = str(job_obj['html'])
            return jsonify(job_obj)
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
    urlToFetch = getValidatedUrl(urlToFetch)
    job_id = job.add_job(urlToFetch)
    fetch_html_task.fetch_html.apply_async(args=[job_id], countdown=0)
    return redirect(url_for('get_job', job_id=job_id))




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)