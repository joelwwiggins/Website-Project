from flask_pymongo import PyMongo
import flask
app = flask.Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://abc:1234@cluster0.7hm4r.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route("/")
def git_top10(name):
    d = job_resume
    df = pd.DataFrame([d[name]]).T
    df.columns = ["value"]
    users=['joel','mason']
    return df.sort_values("value", ascending=False).head(10).to_dict()