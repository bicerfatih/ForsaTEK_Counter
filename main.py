from flask import Flask, render_template

app = Flask(__name__)

# Target date for ForsaTEK event
EVENT_DATE = "2025-06-23 00:00:00"

@app.route('/')
def home():
    return render_template('index.html', event_date=EVENT_DATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)