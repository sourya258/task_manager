# Task Manager API  
A RESTful API built with Flask for task management.  

## Features  
  - User authentication (registration & login)  
  - CRUD operations for tasks  
  - Priority-based task sorting  
  - JWT authentication  
  - PostgreSQL database integration  
  - Hosted on AWS (EC2)  

## Tech Stack  
  - **Backend:** Flask (Flask-RESTful, Flask-JWT-Extended)  
  - **Database:** PostgreSQL  
  - **Hosting:** AWS (EC2)  
  - **Tools:** SQLAlchemy, Flask-Swagger  

## Installation & Setup  

  ### Clone the Repository  
    git clone https://github.com/sourya258/task_manager.git  
    cd task_manager
  
  ### Install Dependencies  
    pip install -r requirements.txt  
  
  ### Set Up Environment Variables   
    DATABASE_URL=postgresql://user:password@localhost/task_manager  
    SECRET_KEY=your_secret_key  
    JWT_SECRET_KEY=your_jwt_secret  
  
  ### Initialize the Database  
    from flask_rest import app, db  
    with app.app_context():  
        db.create_all()  
    
  ### Run the API Locally  
    python flask_rest.py
  
## API Endpoints  
Refer to this link for API endpoints:  
[API Endpoints](https://github.com/user-attachments/assets/ff9648b5-1893-438f-8245-af1e560f1f12)  
