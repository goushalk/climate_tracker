from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render the main page
    return render_template('index.html')

@app.route('/cli_tracker')
def cli_tracker():
    # Render the CLI Tracker page (placeholder for your actual content)
    return render_template('cli_tracker.html')


@app.route('/temprature')
def temprature():
    return render_template('temprature.html')


@app.route('/wind')
def wind():
    return render_template('wind.html')


@app.route('/rain&snow')
def rain_snow():
    return render_template('rain&snow.html')




if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
