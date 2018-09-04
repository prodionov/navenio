# navenio

## Installation

Clone the project
```
$ git clone https://github.com/prodionov/navenio.git
$ cd navenio
```

Create the virtual environment
```
$python3 -m virtualenv myenv
$source myenv/bin/activate
```

Install dependencies from the requirements.txt
```
$pip install -r requirements.txt
```

To start the application
```
python run.py
```
and open localhost:5000 in your browser

## HOW IT WORKS

### Option 1 (remote access).

You can access localhost:5000/remote via Postman or using CURL. It requires basic auth. Use the following credentials:
`username = james
password = agent`

If you use Postman
add credentials and headers `'Content-Type':'application/json'`

<img src="https://user-images.githubusercontent.com/19667238/45017283-2077d880-b01f-11e8-8364-d323b98788f6.png" width="700" />

Send your request and you will receive the result back

<img src="https://user-images.githubusercontent.com/19667238/45017621-f70b7c80-b01f-11e8-8c0b-4ef59c6afad6.png" width="700"/>

### Option 2.
Visit localhost:5000, register on the website manually, login and you will be redirected to a page with a form where you can add request data manually and receive the result on screen.

This option is not practical, as the signal list can be extremely long and cannot be added manually.

### In a few sentences explain what guided you to design the service the way you did and how it can scale. 

I wanted to implement a solution that will allow users to access this service remotely. That way, both the signal and value can be sent in a json format. I used Flask, a microframework for Python, because it is easy to create prototypes with. It is lightweight and has large number of libraries to introduce features, for example flask_basicauth for basic authentication. 

In order to scale this project, I would set it up with uWSGI and Nginx in the cloud (AWS, Digital Ocean or others). Further scaling could be achieved by using technologies like Docker and Google Kubernetes. 





