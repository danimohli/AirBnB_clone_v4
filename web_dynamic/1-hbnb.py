#!/usr/bin/python3
"""
Flask web application for AirBnB clone - Web dynamic.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
import uuid

app = Flask(__name__)


@app.route('/1-hbnb', strict_slashes=False)
def hbnb():
    """
    Display a HTML page with dynamic filters, like 8-index.html, with States,
    Cities, Amenities, and Places.
    """
    states = sorted(storage.all(State).values(),
                    key=lambda state: state.name)
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda amenity: amenity.name)
    places = sorted(storage.all(Place).values(),
                    key=lambda place: place.name)

    # Generate a unique cache ID
    cache_id = uuid.uuid4()

    return render_template('1-hbnb.html', states=states,
                           amenities=amenities, places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
