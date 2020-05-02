from random import choices,choice,sample

from flask import Flask, render_template, g
from data import *

app = Flask(__name__)

@app.route('/')
def main():
    random_tours = sample(tours.items(), 6)
    print(type(random_tours))
    template_context = dict(title=title, subtitle=subtitle, description=description, tours=tours, departures=departures)
    output = render_template("index.html", **template_context)
    return output

@app.route('/departures/<departure>')
def show_dep(departure):

    selected_tours= {}
    for ind, tour in tours.items():
        if tour['departure']==departure:
            selected_tours[ind]=tour

    output = render_template("departure.html", departures=departures, title=title, departure=departure, selected_tours=selected_tours)
    return output

@app.route('/tours/<id>')
def show_tour(id):
    tour=tours[int(id)]
    output = render_template("tour.html", departures=departures, title=title, tour=tour)
    return output

app.run('localhost', 8000)
