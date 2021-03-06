"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members, methods=['GET'])
def getAllMembers():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def getOneMember(member_id):
    members = jackson_family.query.get_member(id)
    return jsonify(member),400


@app.route('/member', methods=['POST'])
def MembersPost():

    members = jackson_family.get_all_members()
    newMember = json.loads(request.data)
           member = _members(
           _name = newMember["_name"],
           last_name = newMember["last_name"],
           age = newMember["age"]
           )
           
    members.append(newMember)
   # newMember = jackson_family.add_member(jackson_family)
    return jsonify(members),


@app.route('/members/<int:member_id>', methods=["DELETE"])
def membersDelete(member_id):
           members = jackson_family.get.all_members()
           members.pop(member.id)
           
           return jsonify(members),200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
