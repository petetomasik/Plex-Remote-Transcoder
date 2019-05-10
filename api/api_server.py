import os
import multiprocessing
import requests
import json

from flask import Flask
api_server = Flask(__name__)

@api_server.route('/')
def index():
    return 'Hello World'

@api_server.route('/ping')
def ping_respond():
    #returns the username
    return str( 'Pong' )

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
    return remote_load_result.json()

@api_server.route('/load/cluster')
def get_cluster_load():
    running_slaves = get_slave_list()
    servers = running_slaves["servers"]
    load_cluster = []
    for server in servers:
        load = ["%0.2f%%" % l for l in get_system_load_remote(server)]
        load_cluster.append("  %15s: %s" % (server, ", ".join(load)))

    return str( load_cluster )

@api_server.route('/list/slaves')
def get_slave_list():
    #config = get_config()
    config = {
            "servers": {
                "localhost", "127.0.0.1"
                }
            }

    return config

@api_server.route('/list/sessions')
def get_session_list():
    #config = get_config()
    config = {
            "sessions": {
                "session1", "session1 details",
                "session2", "session2 details",
                }
            }

    return config

@api_server.route('/auth_token')
def get_auth_token():
    config = {
            "auth_token", "foo_bar"
            }
    return str( config )

if __name__ == "__main__":
  api_server.run()
