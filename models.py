from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = "user"
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(50), nullable=False)
  apellido = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(50), nullable=False, unique=True)
  password = db.Column(db.String(16), nullable=False)

  def serialize(self):
    return {
      'id': self.id,
      'nombre': self.nombre,
      'apellido': self.apellido,
      'email': self.email
    }