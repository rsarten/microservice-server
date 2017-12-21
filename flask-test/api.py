# Product service

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/flask')
def get_people():
	return jsonify({'people':['Eleanor', 'Rory', 'Michael']})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
