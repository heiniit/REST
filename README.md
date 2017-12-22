# REST
Playing with REST (and HTTP) servers/clients

# Usage
To run the whole functionality, start both servers (http and REST) using two separate command prompts:

`> python HttpSrv.py`

and:

`> python RestSrv.py`

Then start browser and go to address http://127.0.0.1/

# What happens
First the HTTP request from the browser goes to the HTTP server. The server loads html page from the file and returns that.

Then, when the test page opens, giving two nombers and clicking "Calc" sends a request to the REST server. The servers does the calculation and returns the result to the web browser.
