from flask import Flask , render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///requestdata.db"
db = SQLAlchemy(app)

class User(db.Model):
    id  =db.Column(Integer, primary_key = True) 
    name = db.Column(String, nullable = False)
    sno = db.Column(Integer,nullable = False)
    
@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        return  request.form['title'] + request.form['desc']
    return render_template('practice.html')

@app.route('/about/<name>/<int:sno>')
def about(name,sno):
    
    user = User(name=name, sno = sno)
    db.session.add(user,sno)
    db.session.commit()
    return f"User {name} {sno} added"

@app.route("/user/<int:sno>")
def get_users(sno):
    user = User.query.get(sno)
    if user:
        return f'User Id: {sno}, Name: {user.name}'
    return 'Not found'

@app.route("/update/<int:sno>/<new_name>")
def update(sno,new_name):
    t_b_updt = User.query.get(sno)
    if t_b_updt:
        t_b_updt.name = new_name
        db.session.commit()
        return f'The sno:{sno} has the name: {t_b_updt.name}'
    return "Couldn't find user"
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print('DataBase Created successfully')
    app.run(debug=True,port=8000)