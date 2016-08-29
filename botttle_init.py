from bottle import route, run, template, get, debug, static_file


@route('/static/:path#.+#', name='static')
def static(path):
  return static_file(path, root='./static')

@route('/')
def index():
  return template('index.html')

debug(True)
run(host='localhost', port=8080)