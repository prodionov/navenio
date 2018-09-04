# navenio

## Instalation

Clone the project
```
$ git clone https://github.com/prodionov/navenio.git
$ cd navenio
```

Create virtual environment
```
$python3 -m virtualenv myenv
$source myenv/bin/activate
```

Install dependencies from the requirements.txt
```
$pip install -r requirements.txt
```

To start an application
```
python run.py
```
and open localhost:5000 in your browser

## HOW IT WORKS

### Option 1 (remote access).

Via Postman or using CURL you can access localhost:5000/remote. It's requires basic auth. Use following credentials:
`username = james
password = agent`

If you use Postman
add credentials and headers `'Content-Type':'application/json'`

<img src="https://user-images.githubusercontent.com/19667238/45017283-2077d880-b01f-11e8-8364-d323b98788f6.png" width="400" />

send request and you will receive the result back

<img src="https://user-images.githubusercontent.com/19667238/45017621-f70b7c80-b01f-11e8-8c0b-4ef59c6afad6.png" width="400"/>

### Option 2.
Visit localhost:5000, register on the website manually, login and you will be redirected to a page with a form where you can add request data manually and receive a result on the screen.

This option is not practical, as signal list can be extremely long and cannot be added manually.

### In a few sentences explain what guided you to design the service the way you did and how it can scale. 

I have done an API service in Flask before, that is set up with uWSGI and Nginx. However, it doesn't require any authentication (normally, other API services would require a KEY). That confused me, and that's why firstly, I have designed a page where a client can register and access a form where he can receive number of value crossings. However, that seemed very impractical. 

So, I decide to implement a solution that will allow a user to access this service remotely. That way, both signal and value can be send over in a json format remotely. 

Finally, one option to scale this project coud be to set it up with uWSGI and Nginx. The step further would be using Docker containers,  





