from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, User
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mibasededatos.db'
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

@app.route('/', methods=['GET'])
def home():
  return jsonify({"message": "Hello, World!"})

@app.route("/getUSer", methods=['GET'])
def get_user():
  usuarios = User.query.all()
  usuarios_serializados = list(map(lambda usuario: usuario.serialize(), usuarios))

  return jsonify({
    "status": "success",
    "data": usuarios_serializados
  }), 200

@app.route("/getUserById/<int:id>", methods=['GET'])
def get_user_by_id(id):
  usuario = User.query.filter_by(id=id).first()
  return ({
    "status": "success",
    "data": usuario.serialize()
  }), 200

@app.route('/createUser', methods=['POST'])
def create():
  data = request.json
  usuario = User()

  print(data['nombre'])
  usuario.nombre = data['nombre']
  usuario.apellido = data['apellido']
  usuario.email = data['email']
  usuario.password = data['password']

  # print(usuario)
  db.session.add(usuario)
  db.session.commit()

  return {
    "message": "User created successfully",
    # "data": usuario
  }, 201




if __name__ == "__main__":
  app.run(host='localhost', port=5002, debug=True)