Build/execution instructions:

You must have Python installed (version 2.7.x recommended).
Also make sure you get the Heroku Toolbelt from http://devcenter.heroku.com/
Install Git as well (make sure to configure global user and ssh public key).

Make sure you have the following environment variables defined:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME
DATABASE_URL
S3_BUCKET_NAME
SEARCHBOX_SSL_URL
SEARCHBOX_URL

Their values can be found be doing a 'heroku config' inside the project folder.

Also make sure all requirements are installed locally by running 'pip install -r requirements.txt' inside
the project folder.
