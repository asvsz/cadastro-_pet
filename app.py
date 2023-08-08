#app.py 

from flask import Flask
from flask_restful import Api
from model.models import db
from model.resources import TutorResource, PetResource


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
api = Api(app)
db.init_app(app)

with app.app_context():
  db.create_all()
  
api.add_resource(TutorResource, '/tutor/<int:tutor_id>', '/atualizarTutor/<int:tutor_id>')
api.add_resource(PetResource, '/pet/<int:pet_id>', '/atualizarPet/<int:pet_id>')

if __name__ == '__main__':
  app.run(debug=True)