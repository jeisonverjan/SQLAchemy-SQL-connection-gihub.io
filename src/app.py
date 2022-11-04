from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Create APP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin123*@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#data base instance
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String (50), unique=True)
    description = db.Column(db.String (100))
    
    def __init__(self, title, description):
        self.title = title
        self.description = description

with app.app_context(): 
    db.create_all()

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'task', 'description')
        
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


@app.route('/task', methods=['POST', 'GET'])
def create_task():
    
    new_task = Task(title='comprar queso', description='comprarlo en el Jumbo')
    db.session.add(new_task)
    db.session.commit()
    
    return '<h3>Task added to the database</h3>'


if __name__ == '__main__':
    app.run(debug=True)