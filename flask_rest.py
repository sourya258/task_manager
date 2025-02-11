from flask import Flask,request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer
from datetime import datetime


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Hello'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"

db = SQLAlchemy(app)
jwt = JWTManager(app)

class Blog(db.Model):
    id = db.Column(Integer, primary_key = True, autoincrement = True)
    title = db.Column(String,nullable = False)
    description = db.Column(String, nullable = False)
    logs = db.Column (String,default = datetime.now)
    
    def __repr__(self):
        return f"{self.id} - {self.title}"
    
users = {}

@app.route("/register", methods = ["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username in users:
        return {"Message" : "User already exists"} , 409
    
    users[username] = password
    
    return {"Message" : "User registered successfully"},201

@app.route("/login", methods = ["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username not in users:
        return {"Message" : "Invalid Input"}, 400
    elif users[username] != password:
        return {"Message" : "Invalid Input"}, 401
    
    access_token = create_access_token(identity=username)
    return{"Access Token" : access_token}

@app.route("/create", methods = ["POST"])
@jwt_required()
def create():
    current_user = get_jwt_identity()
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    Details = Blog(title=title , description = description)
    db.session.add(Details)
    db.session.commit()
    
    return {
        "id": Details.id,
        "title": Details.title,
        "description": Details.description,
        "logs": Details.logs
    }, 201
    
@app.route("/edit/<int:id>", methods = ["GET" , "POST"])
@jwt_required()
def edit(id):
    data = request.get_json()
    title = data.get("title")
    description = data.get("description")
    Details = Blog.query.filter_by(id = id).first()
    
    if not Details:
        return {"Message" : "Blog not found"}, 404
    
    Details.title = title
    Details.description = description
    db.session.commit()
    
    return{"Message" : "Blog updated successfully"  f"id : {id}, title :{title}, description:{description}"},200


@app.route("/delete/<int:id>" , methods = ["DELETE"])
@jwt_required()
def delete(id):
    Details = Blog.query.filter_by(id = id).first()
    if Details:
        db.session.delete(Details)
        db.session.commit()
        return {"Message":"Deleted Successfully"},200
    else:
        return {"Message" : "Invalid Input"},403
    
@app.route("/look", methods = ["GET"])
def look():
    Details = Blog.query.all()
    
    if Details:
        return {"All posts" : [f"{blog.id} - {blog.title} - {blog.description} - {blog.logs} \n" for blog in Details]},201
    else:
        return {"Message" : "No Blogs"}
        
    
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    








