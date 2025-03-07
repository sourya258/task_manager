from flask import Flask,request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required, create_access_token, create_refresh_token, decode_token
from sqlalchemy import String, Integer, VARCHAR, Text, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from datetime import timedelta
from flasgger import Swagger
import uuid
import redis

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:gublu%40sql9@localhost:5432/task_manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'Hello'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=10)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

db = SQLAlchemy(app)
jwt = JWTManager(app)
swagger = Swagger(app)
redis_client = redis.Redis(host = "localhost",port = 6379, decode_responses=True)

limiter = Limiter(get_remote_address,app=app,default_limits = ['5 per minute'])
CORS(app, resources= {r"/api/*":{"origins" : ["http://localhost:5000", "http://127.0.0.1:5000"]}})

#User storage
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(String ,primary_key =True,unique = True, nullable = False, default = lambda: str(uuid.uuid4()))
    email = db.Column(VARCHAR, unique = True, nullable = False)
    password  = db.Column(VARCHAR, nullable = False)
    tasks = db.relationship('Task', backref = "user" ,lazy = True)
    
#Task Storage
class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(Integer,primary_key =True,unique = True, nullable = False,autoincrement = True)
    title = db.Column(Text,nullable = False)
    description = db.Column(Text)
    user_id = db.Column(String, ForeignKey("user.id"), nullable = False)
    
#Using flask for user authentication
@app.route('/',methods = ["POST"])
@limiter.limit("10 per minute")
def register(): 
    """
    Register Or Login
    ---
    parameters:
        - name: Login Or Register
          in: body
          required: true
          schema:
            type: object
            properties:
                email:
                    type: String
                    description: Enter your Email
                password:
                    type: String
                    description: Enter your Password
    responses:
        200:
            description: User affirmed successfully
        401:
            description: Unauthorised
        400:
            description:  Bad Request               
    """ 
    
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    if not email or not password:
        return bad_req(400)
    
    check_user: User = User.query.filter_by(email = email).first()
    
    if check_user and check_password_hash(check_user.password,password):
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)

        return {"Logged In" : {"Access Token" : access_token, "Refresh_Token" : refresh_token}}
    
    elif check_user and not check_password_hash(check_user.password,password):
        return unauth(401)
    
    hashed_password = generate_password_hash(password)
    new_user = User(email=email,password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return {"Success" : "User has been registered succesfully"}


#Regenrating access token
@app.route('/ref', methods = ["POST"]) 
@limiter.limit("1 per minute")
@jwt_required(refresh=True)
def regenrate_access_token():
    """
    Regenerate Access Token
    ---
    parameters:
        - name: Authorization
          in: header
          type: string
          required: true
          description: Enter your access token
          
    responses:
        200:
           description : Successfull
        400:
            description:  Bad Request 
    """  
    current_user = get_jwt_identity()
    if not current_user:
        return bad_req(400)
           
    new_access_token = create_access_token(identity=current_user)
    
    return {"New Access Token" : new_access_token}


#implementing CRUD feautres by restful_api
class Implement(Resource):
    @jwt_required()
    @limiter.limit("50 per minute")
    @jwt_required()
    def post(self):
        """
        Create a Task
        ---
        parameters:
            - name: Authorization
              in: header
              type: string
              required: true
              description: JWT token for authentication
              
            - name: task
              in: body
              required: true
              schema:
                type: object
                properties:
                    title:
                        type: string
                        description: Enter the title of your task
                    desc:
                        type: string
                        description: Enter the description of your task
        responses:
            201:
                description: User affirmed successfully
            401:
                description: Unauthorised
            400:
                description:  Bad Request
        """
        
        current_user = get_jwt_identity()
        data = request.get_json()
        title = data['title']
        desc = data['desc']
        
        if not title:
            return bad_req(400)
        
        recg_usr: User = User.query.filter_by(email=current_user).first()
        if not recg_usr:
            return unauth(401)
        
        new_data = Task(title=title,description = desc,user_id = recg_usr.id)
        db.session.add(new_data)
        db.session.commit()
        
        return {"Success":f"Task created succesfully with id {new_data.id}"},201
    
    @jwt_required()
    @limiter.limit("50 per minute")
    def get(self):
        current_user = get_jwt_identity()
        recg_user : User = User.query.filter_by(email = current_user).first()
        if not recg_user:
            return unauth(401) 
        
        srch_tsk : Task = Task.query.filter_by(user_id = recg_user.id).all()
        if not srch_tsk:
            return nt_found(404)
        
        return {f"{recg_user.email} Tasks " : [{"id":task.id, "title":task.title, "description":task.description} for task in srch_tsk]},201
        
class Implement_2(Resource):
    @jwt_required()
    @limiter.limit("50 per minute")  
    def put(self,task_id):
        """
        Update a Task
        ---
        parameters:
            - name: task_id
              in: path
              type: integer
              required: true
              description: Please enter your task id
              
            - name: Authorization
              in: header
              type: string
              required: true
              description: Enter your access token
              
            - name: Edit Your Task
              in: body
              required: true
              schema:
                type: object
                properties:
                    title:
                        type: string
                        required: true
                        default: "{{tsk_title}}"
                        description: Edit your title
                    desc:
                        type: string
                        default: "{{tsk_description}}"
                        description: Edit your description
        responses:
            201:
                description: User affirmed successfully
            401:
                description: Unauthorised
            404:
                description:  Not Found                
        """
        
        current_user = get_jwt_identity()
        recg_user : User = User.query.filter_by(email = current_user).first()
        if not recg_user:
            return unauth(401)
        
        srch_tsk : Task = Task.query.filter_by(id = task_id, user_id = recg_user.id).first()
        if not srch_tsk:
            return nt_found(404)
        
        
        data = request.get_json()
        title = data['title']
        desc = data['desc']
        
        if not title:
            return nt_found(404)
        
        srch_tsk.title = title
        srch_tsk.description = desc
        db.session.commit()
        
        return {"Success" : f"Todo Updated Successfuly . Id - {srch_tsk.id}"} , 201
        
    @jwt_required()
    @limiter.limit("50 per minute")
    @jwt_required()
    def delete(self, task_id):
        """
        Delete a Task
        ---
        parameters:
            - name: Authorization
              in: header
              type: string
              required: true
              description: Enter your access token
              
            - name: task_id
              in: path
              type: integer
              required: true
              description: Deleting a Task
        responses:
            
            401:
                description: Unauthorized
            404:
                description: Not found
            201:
                description: Success        
        """
        
        current_user = get_jwt_identity()
        recg_usr : User = User.query.filter_by(email = current_user).first()
        if not recg_usr:
            return unauth(401)
        
        srch_tsk : Task = Task.query.filter_by(id = task_id, user_id = recg_usr.id).first()
        if not srch_tsk:
            return nt_found(404)
        
        db.session.delete(srch_tsk)
        db.session.commit()
        return {"Success" : "Task deleted successfully"},201
            
api.add_resource(Implement,'/task')
api.add_resource(Implement_2,'/task/<int:task_id>')

@app.errorhandler(400)
def bad_req(error):
    return {"Error" : "Bad request"} , 400

@app.errorhandler(401)
def unauth(error):
    return {"Error" : "Unauthorized"} , 401  

@app.errorhandler(404)
def nt_found(error):
    return {"Error" : "Not found"} , 404      
    
if __name__=='__main__':
    app.run(debug=True)





















# '''from flask import Flask, render_template, session, request, redirect, jsonify, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# from sqlalchemy import String, Integer, ForeignKey
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity



# app = Flask(__name__)
# jwt = JWTManager(app)
# app.config['JWT_SECRET_KEY'] = "Hello"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///to.db"
# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

# class User(db.Model):
#     id = db.Column(Integer, primary_key = True)
#     email = db.Column(String,nullable = False, unique = True)
#     password = db.Column(String,nullable =False)
#     todo = db.relationship("TODO", backref = "user", lazy = True)
    
# class TODO(db.Model):
#     id = db.Column(Integer, primary_key = True)
#     title = db.Column(String, nullable = False)
#     desc = db.Column(String, nullable = False)
#     user_id = db.Column(Integer,ForeignKey("user.id"),nullable = False)


# @app.route("/register", methods = ["POST"])
# def register():
#     data = request.get_json()
#     email = data.get("email")
#     password = data.get("password")
    
#     if not email or not password:
#         return {"Message" : "Invalid Username or Password"},400
    
#     if User.query.filter_by(email=email).first():
#         return {"Message" : "User already exists"},409
    
    
#     hashed = bcrypt.generate_password_hash(password).decode("utf-8")
#     verify_user = User(email = email, password = hashed)
    
#     db.session.add(verify_user)
#     db.session.commit()
#     return {"Message" : "User registered successfully"},201

# @app.route("/login", methods = ["GET", "POST"])
# def login():
#     data  =request.get_json()
#     email = data["email"]
#     password = data["password"]
    
#     if not email or not password:
#         return {"Message" : "Invalid Username or Password"},400
    
#     verify_user: User = User.query.filter_by(email=email).first()
#     if not verify_user or not bcrypt.check_password_hash(verify_user.password,password):
#         return {"Message" : "Invalid Credentials"},401
    
    
#     access_token = create_access_token(identity=email)
#     return {"Access Token" : access_token},200
    
# @app.route("/create" , methods = ["GET", "POST"])
# @jwt_required()
# def create():
#     current_user = get_jwt_identity()
#     info = request.get_json()
#     title = info["title"]
#     desc = info["desc"]
    
#     user: User= User.query.filter_by(email=current_user).first()
#     if not user:
#         return {"Message" : "User not found"}
    
#     if not title:
#         return {"Message" : "No title, Please enter title"},400
    
#     new_todo = TODO(title = title, desc =desc, user_id = user.id) 
#     db.session.add(new_todo)
#     db.session.commit()
    
#     return {"Message" : f"Todo Created Successfully , id : {new_todo.id}"}

# @app.route("/edit/<int:todo_id>", methods=["POST"])
# @jwt_required()
# def edit(todo_id):
#     current_user = get_jwt_identity()
#     info = request.get_json()
#     title = info["title"]
#     desc = info["desc"]
    
#     user : User = User.query.filter_by(email=current_user).first()
#     if not user:
#         return{"Message" : "User doesn't exist"},404
    
#     todo : TODO= TODO.query.filter_by(id = todo_id, user_id = user.id).first()
    
#     if not todo:
#         return {"Message" : "Todo not found"},404
    
#     todo.title = title
#     todo.desc = desc
#     db.session.commit()
#     return {"Message" : "Todo updated successfully"}
    
    
# @app.route("/delete/<int:todo_id>", methods = ["POST", "GET"])
# @jwt_required()
# def delete(todo_id):
#     current_user = get_jwt_identity()
#     user :User  = User.query.filter_by(email=current_user).first()
    
#     if not user:
#         return {"Message" : "User doesn't exist"}, 404
    
#     todo = TODO.query.filter_by(id = todo_id, user_id = user.id).first()
#     if not todo:
#         return {"Message" : "Todo deleted succesfully"}
    
#     db.session.delete(todo)
#     db.session.commit()
#     return {"Message" : "Deleted successfully"}
    




    
    
    
    
    




    
# if __name__ == "__main__":
#     app.run(debug=True)
     
#      '''