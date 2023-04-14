# -*- coding: utf-8 -*-
"""

@author: sebis
"""

from flask import Flask
from flask_dialogflow.agent import DialogflowAgent
from neo4j import GraphDatabase
from pymongo import MongoClient
from datetime import datetime

# create app and agent instances
app = Flask(__name__)
agent = DialogflowAgent(app=app, route="/", templates_file="templates/responses.yaml")
# driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "password1"))
driver = GraphDatabase.driver("neo4j+s://93654760.databases.neo4j.io:7687",
                              auth=("neo4j", "eL3USAYn1EhqffS-A66kChm8E3syWkF3p4FrSHR3E68"))

mongo_uri = "mongodb+srv://nilsrehtanz:kGLThHw9ljQzAosQ@news-agent-logs.xblynv5.mongodb.net/test"
client = MongoClient(mongo_uri)
db = client["logs_database"]
logs_collection = db["logs"]
state_collection = db['state']


# set up test route
@app.route("/")
def index():
    return "<h1>News Agent Backend</h1>"


# import main conversation handlers for webhooks
from app import webhooks
