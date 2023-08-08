from flask_restful import Resource, reqparse
from model.models import db, Tutor, Pet


class TutorResource(Resource):
  def get(self, tutor_id):
    tutor = Tutor.query.get(tutor_id)
    return tutor
  
  def put(self, tutor_id):
    args = parser.parse_args()
    tutor = Tutor.query.put(tutor_id)
    return tutor

class PetResource(Resource):
  def get(self, pet_id):
    pet = Pet.query.get(pet_id)
    return pet
  