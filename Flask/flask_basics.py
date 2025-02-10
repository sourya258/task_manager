from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"

db = SQLAlchemy(app)  # Attach db to app

class Todo(db.Model):
    sno = db.Column(Integer, primary_key=True)
    title = db.Column(String, nullable=False)
    desc = db.Column(String, nullable=False)
    datetime = db.Column(String, default=datetime.now)

    def __repr__(self):
        return f'{self.sno} - {self.title}'
    
@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Todo(title = title, desc = desc)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all()
    return render_template('home.html', allTodo = allTodo)

@app.route('/update/<int:sno>', methods = ['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo = todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return 'This is og'


# ✅ Create tables inside an app context (This prevents errors)
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")  # Debugging message
    app.run(debug=True)
