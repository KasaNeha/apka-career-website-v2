from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Scientist',
    'location': 'Bengaluru,India',
    'salary': 100000
}, {
    'id': 2,
    'title': 'Data Analyist',
    'location': 'Delhi,India',
    'salary': 150000
}, {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'Chennai,India',
    'salary': 170000
}]

# First url---first html route
@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)

# Second url----first api route
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

