from app import app

@app.route("/")
def frontend_index():
    return app.send_static_file("index.html")
