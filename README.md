# ZBCE FastAPI REST API Mockup

A REALLY basic REST API to illustrate the basic features of FastAPI. Only weight endpoints are implemented.

## Basic Features
- Modularizable file structure
- Automatically generating documentation
- It's fast
- Input verification through Pydantic schemas
- It's better than Flask

## File Structure 
- app/routers : Handle HTTP requests and route them to proper controller
- app/controllers : take request object, pull out data from request, validate, then send to service(s)
- app/models : Classes and instances that interact with database
- app/schemas : Schemas for API requests/responses
- app/services : Contains business logic as well as well as access to database
- app/config.py : reads enviromental variables from .env file
- .env : (Not here because you need to add it yourself) Contains all the secret keys and other stuff
- app/main.py : Connects everything together

## Installation

<b>Create Python 3 virtual environment</b>

```
python3 -m venv env
```

<b>Activate virtual enviroment</b>

On Windows,
```
env/Scripts/activate.bat
```

On Linux or MacOS,
```
source env/bin/activate
```

<b>Install required libraries</b>
```
pip install -r requirements.txt
```

<b>Create .env file</b>

Create .env file with the contents. Fill it the key with your appropriate username and password.
```
SQLALCHEMY_DATABASE_URL="mysql+pymysql://USERNAME:PASSWORD@localhost/zotbinsCE"
```

## Starting the FastAPI server

After completing all the steps, run the command
```
uvicorn app.main:app --reload
```
Make sure you activated your virtual environment before running the command else the command wil fail

If the server succesfully started, you are all done! 

You can look at the automatically generated docs at http://127.0.0.1:8000/