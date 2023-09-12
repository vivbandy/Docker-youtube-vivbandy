# Import necessary modules from the pytube and flask libraries
from pytube import Search
from flask import Flask, render_template_string

# Create a new Flask web server instance. The __name__ variable denotes the name of the current module.
# This is needed so that Flask knows where to look for templates, static files, and so on.
app = Flask(__name__)

# Define a route for the root URL ("/") of the web server
@app.route('/')
def index():
    # Search YouTube for videos with the query 'elden ring'
    search_results = Search('elden ring').results
    
    # Sort the search results by the number of views in descending order and take the top 10
    sorted_videos = sorted(search_results, key=lambda x: x.views, reverse=True)[:10]
    
    # Render and return an HTML template string to display the videos
    # The template uses Flask's built-in templating engine (Jinja2) to loop through the sorted_videos and display them
    return render_template_string("""
    <ul>
    {% for video in videos %}
        <li><a href="{{ video.watch_url }}">{{ video.title }}</a> - {{ video.views }} views</li>
    {% endfor %}
    </ul>
    """, videos=sorted_videos)

# Check if this script is being run as the main module and not being imported elsewhere
if __name__ == "__main__":
    # If the script is the main module, start the Flask web server in debug mode
   import os
   port = int(os.environ.get("PORT", 8080))
   app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
