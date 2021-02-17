# TrustIT

Task 2 - plan:

## Flow
- The monitored repository should include a workflow attached to it's CI system, e.g. a 'Github actions' workflow.
- On trigger (merger of PR to main branches), a server (a pre-defined container) is initialized and pulls the log and screenshot of the PR. This step can be possibly implemented serverless (FaaS).
- The log and screenshot is saved to a storage system (e.g. Amazon S3). The paths (urls) to the storage and other data is saved in a db.
- At a user's access to the dashboard the database is pulled and presents a list of <id, log, image> tuples. 

## Backend
- Env: use requirements.txt to create env on your instance/docker
- Written in python with a flask (sql db using flask-sqlalchemy) framework.
- DB is a PostgreSQL (or any SQL) table with a <id:id (key), screenshot_path:url, log_path:url, date:datetime> scheme. 
- In the future dataset will include other tables (E.g. Users, NOSQL db).

1. Access to repository is done by using "GitHub REST API v3". For logs and other user and repo related data.

2. Screenshot feature was implemented using the selenium framework and requires a chromedriver in order to properly work:
  i. Check the version of Google Chrome in About Chrome section
  ii. download chromedriver (https://chromedriver.chromium.org/downloads)
  iii. add chromedriver to PATH

## Frontend
- React JS
