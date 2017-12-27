import feedparser
from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route('/news')
def get_news():
	feed = feedparser.parse(BBC_FEED)
	return render_template("news_items.html", articles = feed['entries'])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
