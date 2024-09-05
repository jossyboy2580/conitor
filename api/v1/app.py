#!/usr/bin/python3
"""
My api for the conitor app
"""
from flask import Flask, jsonify, request, abort
import models
from models.pool import Pool
from models.people.collector import Collector
from models.people.participant import Participant
from models.savings import SavingCampaign, Saving


storage = models.storage
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def homepage():
    """the home of the api"""
    return "This is the homepage"

@app.route('/collectors', methods=['GET', 'POST'], strict_slashes=False)
def get_all_collectors():
    """ get all the colectors """
    if request.method == 'POST':
        if not request.is_json:
            return "Wrong json format"
            # abort(404)
        data = request.get_json()
        try:
            firstname = data['firstname']
            lastname = data['lastname']
            email = data['email']
            password = data['password']
            new_collector = Collector(
                        firstname = firstname,
                        lastname = lastname,
                        email = email,
                        password = password
                    )
        except Exception as exc:
            #return jsonify(data)
            return f"Error: {exc}"
            # abort(404)
        else:
            new_collector.save()
            return jsonify(new_collector.id), 201
        
        return jsonify(data), 201
    elif request.method == 'GET':
        collectors = models.storage.all(Collector)
        if collectors:
            collectors = [collector.to_dict() for collector in collectors.values()]
            return collectors
        else:
            abort(400)
    else:
        abort(404)

@app.route('/collectors/<collector_id>/pools', methods=['GET','POST'],
            strict_slashes=False)
def get_or_make_pool(collector_id):
    """ Get pools associated with a collector or make one """

    # Fetching pools associated with this collector
    if request.method == 'GET':
        collector = models.storage.get(Collector, collector_id)
        if not collector:
            abort(400)
        all_pools = models.storage.all(Pool)
        collector_pools = [pool.to_dict() for pool in all_pools
                           if pool.collector_id == collector_id]
        return jsonify({'pools': collector_pools}), 200
    
    # Creating (POSTING) a new pool for this user
    elif request.method == 'POST':
        if not request.is_json:
            abort(400)
        data = request.get_json()
        collector = models.storage.get(Collector, collector_id)
        if not collector:
            return 'not a valid collector'
        new_pool = collector.create_pool(**data)
        if not new_pool:
            return 'pool not created'
        new_pool.save()
        return jsonify(new_pool.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
