from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

# In-memory database
alerts = []

@app.route('/')
def home():
    return render_template('index.html', alerts=alerts)

@app.route('/submit_alert', methods=['POST'])
def submit_alert():
    alert_type = request.form.get('alert_type')
    description = request.form.get('description')
    time_reported = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alerts.append({'type': alert_type, 'description': description, 'time': time_reported})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
