from flask import Flask

from tasks import start_job
app = Flask(__name__)

@app.route("/")
def index():
    return "homepage"

start_job()
if __name__ == "__main__":
    app.run()