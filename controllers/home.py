from flask import Blueprint, jsonify, request, send_from_directory, render_template

app = Blueprint('child', __name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/statics/<path:path>')
def send_statics(path):
    return send_from_directory('statics', path)
    