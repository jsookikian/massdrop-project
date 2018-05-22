# Massdrop Project

#Description
This project is a flask server which uses a worker queue to fetch data from a URL and store the results in a mySQL Database using SQLAlchemy. There is an exposed REST API for adding jobs and checking their status / results.

The homepage contains a form for which a URL should be submitted, and upon submission the job id is returned back to the user in JSON format.

The user can access the job status a the following endpoint:

```
http://localhost:5000/job/<id>
```


# Installation
This project depends on >python3.0 and virtualenv being installed

Clone the repo
```
https://github.com/jsookikian/massdrop-project.git && cd massdrop-project
```

Run the configure script
```

```


