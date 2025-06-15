from flask import Flask, render_template, jsonify
import datetime, json

app = Flask(__name__)

def load_appointments():
    with open('appointments_mock.json') as f:
        items = json.load(f)
    today = datetime.date.today().isoformat()
    return [i for i in items if i['date'] == today]

@app.route('/')
def index():
    appts = load_appointments()
    return render_template('index.html', appointments=appts)

@app.route('/api/appointments')
def appts_api():
    return jsonify(load_appointments())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
