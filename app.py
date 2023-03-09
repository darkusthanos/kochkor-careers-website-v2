from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title': 'Frontend Developer',
    'location' :'Kant, Kyrgyzstan',
    'salary': '60000som'
  },
  {
    'id':2,
    'title': 'DevOps Developer',
    'location' :'Osh, Kyrgyzstan',
    'salary': '30000som'
  },
  {
    'id':3,
    'title': 'Backend Developer',
    'location' :'Bishkek, Kyrgyzstan',
    'salary':"120000som"
  },
  {
    'id':4,
    'title': 'Data Scientist',
    'location' :'Naryn, Kyrgyzstan',
    'salary': '150000som'
  },
]

@app.route("/")
def hello_kochkor():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name='Kochkor')

@app.route("/api/jobs")
def list_lobs():
  return jsonify(JOBS)
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
