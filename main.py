#!.venv/bin/python
from flask import Flask, jsonify, render_template, request
from waitress import serve
import os


from controllers import insurance_sugestion

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['POST'])

def index():
    msg = insurance_sugestion(request.get_json())
    if 'ERROR' in msg:
        return jsonify(msg), 400
    return jsonify(msg)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

if __name__ == '__main__':
    serve(app)
