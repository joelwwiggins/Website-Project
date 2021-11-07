# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from numpy.core.function_base import logspace
import pandas as pd
import pymongo


app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb+srv://abc:1234@cluster0.7hm4r.mongodb.net/job_resume?retryWrites=true&w=majority"
# mongo = PyMongo(app)
# # conn = "mongodb+srv://abc:1234@cluster0.7hm4r.mongodb.net/job_resume?retryWrites=true&w=majority"
# client = PyMongo.MongoClient(conn)
# db = client.job_resume

conn = "mongodb+srv://abc:1234@cluster0.7hm4r.mongodb.net/job_resume?retryWrites=true&w=majority"
client = pymongo.MongoClient(conn)
db = client.job_resume
d = db.cos_sim.find({})
a = [x for x in d]
job_resume = a[0]

def git_top10(name):
    d = job_resume
    df = pd.DataFrame([d[name]]).T
    df.columns = ["Cosine Similarity Score"]
    df2= df.sort_values("Cosine Similarity Score", ascending=False).head(10)
    return df2

git_top10("Joel")
# Route to render index.html template using data from Mongo
@app.route("/")
def home():
   # Find one record of data from the mongo database
    # cos_sim = mongo.db.cos_sim.find_one()


    
    # Return template and data
    return render_template("index.html", options=["Joel", "Mason", "Anderson", "Jake"])

@app.route("/data/<name1>")
def get_table(name1):
   # Find one record of data from the mongo database
    # cos_sim = mongo.db.cos_sim.find_one()


    
    # Return template and data
    return render_template("index2.html", options=["Joel", "Mason", "Anderson", "Jake"], data=git_top10(name1).to_html())



# @app.route("/scrape")
# def scrape():
  
#     resume_dict = mongo.db.resume
    
#     # # Update the Mongo database using update and upsert=True
#     # resume_dict.update({}, mars_data, upsert=True)
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)