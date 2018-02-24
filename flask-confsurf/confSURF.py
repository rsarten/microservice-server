from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
from Table import Table

app = Flask(__name__)
CORS(app)

def make_table(vars):
	vars = vars.split(",")
	surf = Table(vars)
	surf.confidentialise()
	return surf.getSURFAsDict()


@app.route('/confSURF/api/v1/table/<path:vars>')
def create_html_table(vars=None):

	surf = make_table(vars)
	return render_template("surf_table.html", table = surf)


@app.route('/confSURF/api/v1/json/<path:vars>')
def create_json_table(vars=None):

	surf = make_table(vars)
	return jsonify(surf)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
