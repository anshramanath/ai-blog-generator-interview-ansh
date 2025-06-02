from flask import Flask, request, jsonify
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler
import os, datetime
import requests

from ai_generator import generate_post
from seo_fetcher import fetch_seo_data

load_dotenv()
app = Flask(__name__)

# Create a folder to save posts
os.makedirs("generated", exist_ok=True)

@app.route("/generate", methods=["GET"])
def generate():
    keyword = request.args.get("keyword")
    if not keyword:
        return jsonify({"error": "Missing keyword"}), 400

    seo = fetch_seo_data(keyword)
    if seo is None:
        return jsonify({"error": f"Keyword '{keyword}' is not supported."}), 400

    blog_post = generate_post(keyword, seo)

    filename = f"generated/{keyword.replace(' ', '_')}_{datetime.date.today()}.md"
    with open(filename, "w") as f:
        f.write(blog_post)

    return jsonify({
        "keyword": keyword,
        "seo": seo,
        "message": "Blog post generated and saved.",
        "file": filename
    })

# Scheduler to run daily
def scheduled_job():
    keyword = "wireless-earbuds"
    url = f"http://127.0.0.1:5000/generate?keyword={keyword}"

    try:
        response = requests.get(url)
        print(f"[Scheduled] Status: {response.status_code}, Response: {response.json()}")
    except Exception as e:
        print(f"[Scheduled] Error calling /generate: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_job, "interval", days=1, next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=10))
scheduler.start()

if __name__ == "__main__":
    app.run(debug=False)