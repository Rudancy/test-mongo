import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'MyNumberTest'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tpa55@mycluster-qbgul.mongodb.net/MyNumberTest?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/info')
def get_tasks():
    numbers=mongo.db.Numbers.find()
    print(numbers)
    return render_template('support.html', numbers=numbers)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)