# Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://abc:1234@cluster0.7hm4r.mongodb.net/job_resume?retryWrites=true&w=majority"
mongo = PyMongo(app)


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
   
    # Find one record of data from the mongo database
    resume_db = mongo.db.resume.find_one()
    # Return template and data
    return render_template("index.html", resume=resume_db)



# @app.route("/scrape")
# def scrape():
  
#     resume_dict = mongo.db.resume
    
#     # # Update the Mongo database using update and upsert=True
#     # resume_dict.update({}, mars_data, upsert=True)
#     return redirect("/")

if __name__ == "__main__":
    app.run()