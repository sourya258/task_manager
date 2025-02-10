from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = "Hello"

users = {  
}

@app.route("/register" , methods = ["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username in users:
        return {"Message" : "Username Exists"},409
    
    users[username] = password
    return {"Message" : "User registered successfully"},201

@app.route("/login",methods = ["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username not in users:
        return {"Message" : "Invalid input"},400
    elif users[username] != password:
        return {"Message" : "Invalid input"},403
    
    access_token = create_access_token(identity=username)
    return {"Message" : f"{username} you have been recognised" , "Access_Token" : access_token },200

@app.route("/protected", methods = ["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return {"Message" : f"Hello {current_user}"}
    
if __name__ == "__main__":
    app.run(debug=True)
    
    