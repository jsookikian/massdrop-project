# Massdrop Project

#Description
This project is a flask server which uses a worker queue to fetch data from a URL and store the results in a mySQL Database using SQLAlchemy. There is an exposed REST API for adding jobs and checking their status / results.

The homepage contains a form for which a URL should be submitted, and upon submission the job id is returned back to the user in JSON format.

The user can access the job status a the following endpoint:

```
http://localhost:5000/job/<id>
```


# Installation
This project depends on >python3.0, virtualenv, and redis  being installed

Clone the repo
```
git clone https://github.com/jsookikian/massdrop-project.git && cd massdrop-project
```

Create a virtual environment, and install requirements
```
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

Start the redis server
```
redis-server
```
 
Start up the celery workers
```
cd src && celery -A app.celery worker  > /dev/null 2>&1 &
```

Start the server
```
python3 src/app.py
```