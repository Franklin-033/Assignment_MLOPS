# Flask web server

from flask import Flask, render_template_string
import redis

app = Flask(__name__)

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def index():
    redis_client.lpush('page_hits', 1)

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My First Web Application</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <div class="container">
            <header>
                <h1>Welcome To My Web Application</h1>
            </header>
            <section class="Bio">
                <h2>About Me</h2>
                <p><strong>Name:</strong> Prasad Malai</p>
                <p><strong>Roll No:</strong> 2023MCS320002</p>
                <p><strong>Bio:</strong> I am a software engineer pursuing MTech from IIIT Kottayam, with specialization in Big Data & ML.</p>
                <p><strong>Current organization:</strong> HL Klemove Automotive</p>
            </section>
            <footer>
                <p>&copy; 2025 Prasad Malai. All rights reserved.</p>
            </footer>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html_content)

@app.route('/hits')
def hits():
    try:
        with open('/data/hits.log', 'r') as log_file:
            hits = log_file.readlines()
    except FileNotFoundError:
        hits = []
    
    return f"<h1>Total Hits: {len(hits)}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
