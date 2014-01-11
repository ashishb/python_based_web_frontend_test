import flask

# Init.
app = flask.Flask(__name__)
# config
app.config.update(SECRET_KEY='a_secret_for_some_internal_use')

@app.route('/path1/')
def path1():
  return 'It works', 200

@app.route('/path2/<ip>')
def path2(ip):
  return 'It works with ip.', 200


def main():
  app.debug = True
  port = 1025
  print 'Starting plain-text HTTP server on port %d.' % port
  app.run(host='0.0.0.0', port=port, threaded=True)


if __name__ == '__main__':
  main()

