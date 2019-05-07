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

if __name__ == "__main__":
  api_server.run()
