import os
import multiprocessing
import requests

from flask import Flask
api_server = Flask(__name__)

@api_server.route('/')
def index():
    return 'Server Works!'

@api_server.route('/greet')
def say_hello():
    return 'Hello from Server'

@api_server.route('/user/<username>')
def show_user(username):
    #returns the username
    return 'Username: %s' % username

@api_server.route('/post/<int:post_id>')
def show_post(post_id):
    #returns the post, the post_id should be an int
    return str(post_id)

@api_server.route('/load/local')
def get_system_load_local():
    nproc = multiprocessing.cpu_count()
    load  = os.getloadavg()
    return str( [l/nproc * 100 for l in load] )

@api_server.route('/load/remote/<host>')
def get_system_load_remote(host):
    remote_load_result = requests.get("http://%s:5000/load/local" % host)
    return str( remote_load_result.json() )

if __name__ == "__main__":
  api_server.run()
