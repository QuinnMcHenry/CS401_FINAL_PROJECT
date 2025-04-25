# Running TheBus Webiste! 🚌

Below are the instructions needed to run our website created as our final project in CS 401: Software Engineering and Design.

In this assignment, we used Docker to containerize 2 python files, routes.py and test_routes.py. 
When app.py runs, a Flask app starts, allowing for the user to use the API from their local device by URL. 
The test_app.py is used to ensure the accuracy of app.py using pytest. Below are instuctions how to run this webiste on your local device.  

## Before You Begin! 📩
To begin, you are provided with these files in this GitHub Repostitory. Download them onto your local device. 

#### Dockerfile
#### routes.py
#### test_routes.py
#### requirements.txt
#### (put name of htmls here and raw data)

![Unknown](https://github.com/user-attachments/assets/fdb25b2b-b803-44d8-bb16-e47aefb3ed5d)


Once Docker is up and running, locate your Terminal and enter the commands below based on your username.


## Building Image from the Dockerfile

Example
```bash

```
Template
```bash
docker build -t <dockerhubusername>/<code>:<version> <dockerfile> . 
```
#

## Running the API (app.py) on port 5001

Example
```bash

```
Template
```bash
docker run --rm -v <directory>:<location> -p <port> <dockerhubusername>/<code>:<version> <pythonversion> <script>
```

Resulting Output Example (PUT NEW HERE)
```bash
 * Serving Flask app 'app'
 * Debug mode: on
INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
INFO:werkzeug:Press CTRL+C to quit
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 721-006-464
```

#

You are all set!
