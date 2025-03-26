from flask import Flask, render_template,jsonify

app = Flask(__name__)

Jobs = [{
    'id': 1,
    'title': "Software Engineer",
    'location': "Banglore, India",
    'salary': "Rs 10,00,000"
}, {
    'id': 2,
    'title': "Backend Engineer",
    'location': "Pune, India",
    'salary': "Rs 15,00,000"
}, {
    'id': 3,
    'title': "Data Scientist",
    'location': "Hyderabad, India",
    'salary': "Rs 14,00,000"
}, {
    'id': 4,
    'title': "Frontend Engineer",
    'location': "Newyork, USA",
    'salary': "$ 10,000"
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=Jobs, company_name="Kronos")

@app.route("/api/jobs")
def jobs_list():
    return jsonify(Jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
