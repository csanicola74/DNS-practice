from flask import Flask, render_template
import Flask
app = Flask(__name__)


@app.route('/home')
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
