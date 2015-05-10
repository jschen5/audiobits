from flask import Flask, send_file, send_from_directory
app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/js/<path:path>')
def send_js(path):
  return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
  return send_from_directory('css', path)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
