from flask import Flask, render_template, g
from data import *

app = Flask(__name__)

@app.context_processor
def dep_to_base():
    return dict(departures=g.departures)

@app.route('/')
def main():
    template_context = dict(title=title, subtitle=subtitle, description=description, tours=tours)
    output = render_template("index.html", **template_context)
    return output

@app.route('/departures/<departure>')
def show_dep(departure):
    output = render_template("departure.html")
    return output

@app.route('/tours/<id>')
def show_tour(id):
    output = render_template("tour.html")
    return output

app.run('localhost', 8000)
