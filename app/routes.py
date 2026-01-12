from flask import Blueprint, jsonify, request
from config import db
from .models import Episode, Guest, Appearance

api = Blueprint("api", __name__)

# GET /episodes
@api.route("/episodes")
def episodes():
    episodes = Episode.query.all()
    return jsonify([e.to_dict(only=("id", "date", "number")) for e in episodes])


# GET /episodes/<id>
@api.route("/episodes/<int:id>")
def episode_by_id(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify(episode.to_dict())


# GET /guests
@api.route("/guests")
def guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict(only=("id", "name", "occupation")) for g in guests])


# POST /appearances
@api.route("/appearances", methods=["POST"])
def create_appearance():
    data = request.get_json()

    try:
        appearance = Appearance(
            rating=data["rating"],
            episode_id=data["episode_id"],
            guest_id=data["guest_id"]
        )
        db.session.add(appearance)
        db.session.commit()

        return jsonify(appearance.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["validation errors"]}), 400

