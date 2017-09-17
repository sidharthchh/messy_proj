# messy_proj
# Introduction

Write about your project in this area.

# Developer Guide

## Getting Started

### Prerequisites
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql]()
- [mysql]()
- [redis]()

### Initialize the project
Create and activate a virtualenv:

```bash
virtualenv venv
source venv/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
NOTE: After installing dependencies, pip-tools is also installed. You can now use it to manage package dependencies of your project.
```bash
'''
Add a new package to requirements.in and run the following command to auto-update requirements.txt file
'''
pip-compile requirements.in

'''
Run the following command to sync your virtualenv
'''
pip-sync
```
 For more details, https://github.com/nvie/pip-tools

Migrate, create a superuser, and run the server:
```bash
python manage.py migrate
python manage.py makemigrations messy
python manage.py createsuperuser
python manage.py runserver
```

## Setting up Environment Variables
Edit the environment variables in **'.env.template'** file and then **RENAME** the file to **'.env'**

NOTE: This file has already been added to .gitignore, hence it will not be pushed to your repository.
While deployment or using CI tools like travis or circle-ci, you have to take care of setting the environment variables seperately.

## Database setup
This project uses dj-database-url library to setup databases. Use the  **DATABASE_URL** environment variable to configure your Django application. set this environment variable with the complete database url.
For more info: https://github.com/kennethreitz/dj-database-url

## Email server setup
This project uses dj-email-url library to setup email servers.
Provide your smtp server url in the **EMAIL_URL** environment variable.
For more info: https://github.com/migonzalvar/dj-email-url

## Static Files
There's a 'static' directory configured already inside the project that is to be used to keep satic JavaScript, CSS, etc files to be used in templates.

## Running test Cases
Some test cases have been included in the authentication/test directory.
Use the following command to run test cases in all apps.

```bash
python manage.py test
```

## Travis-CI Setup
If Travis is setup, then use the **.travis.yml** file in the project root directory to configure travis settings, setting up test environment for travis etc.
For more info on travis, https://travis-ci.org/

## Circle-CI Setup
If Circle-CI is setup, then it takes most of the settings from the project itself, but still there is a circle.yml file included at the project root for configuration.
for more info, https://circleci.com/docs/language-python/


# Deployment Guide




## Setting up Elastic Beanstalk
EBS deployment requires a config file in .ebextensions in the main folder. A `messy.config` is already present which handles basic functions on deployment like migration and serving static files. These configurations can always be changed on need basis.

Follow EBS [documentation](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) on deployment for better understanding.

Following steps need to be undertaken to deploy to AWS EBS(Elastic beanstalk):
  1. Create an account on AWS if not already.
  2. Go to the Elastic Beanstalk management console to create a new application. Add the configurations as required by the application.

#### Deployment to EBS via terminal
  1. Run `source venv/bin/activate` to activate virtual environment.
  2. Run `pip install -r requirements.txt`.
  3. Test the app locally using `python manage.py runserver` and hitting healthCheck url.
  4. Install the awsebcli package using `pip install awsebcli`.
  5. To initialize your application and configuring your environment run `eb init`. (required only for the first time)
  6. Run `eb deploy` to deploy to EBS.

You can configure your environment variables in the configuration settings of the Elastic Beanstalk console.



## Viewing Logs




### Elastic BeanStalk (EBS)
EBS deployment requires a config file in .ebextensions in the main folder. A `messy.config` is already present which handles basic functions on deployment like migration and serving static files. These configurations can always be changed on need basis.

Follow EBS [documentation](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html) on deployment for better understanding.

Following steps need to be undertaken to deploy to AWS EBS(Elastic beanstalk):
  1. Create an account on AWS if not already.
  2. Go to the Elastic Beanstalk management console to create a new application. Add the configurations as required by the application.

#### Deployment to EBS via terminal
  1. Run `source venv/bin/activate` to activate virtual environment.
  2. Run `pip install -r requirements.txt`.
  3. Test the app locally using `python manage.py runserver` and hitting healthCheck url.
  4. Install the awsebcli package using `pip install awsebcli`.
  5. To initialize your application and configuring your environment run `eb init`. (required only for the first time)
  6. Run `eb deploy` to deploy to EBS.

You can configure your environment variables in the configuration settings of the Elastic Beanstalk console.



## Revert Build


# Troubleshooting
