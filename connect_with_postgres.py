from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:211218@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = '571ebf8e13ca209536c29be68d435c00'

db = SQLAlchemy(app)

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(120), nullable=False)

    def __init__(self, pname, color):
        self.pname = pname
        self.color = color


class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100), nullable = False)
    user_email = db.Column(db.String(100), nullable= False)
    user_password = db.Column(db.String(150), nullable = False)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@app.route('/')
def home():
    return '<a href="/addperson"><button> Click here </button></a>'


@app.route("/addperson")
def addperson():
    return render_template("index.html")


@app.route("/personadd", methods=['POST'])
def personadd():
    pname = request.form["pname"]
    color = request.form["color"]
    entry = People(pname, color)
    db.session.add(entry)
    db.session.commit()

    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    #check the request method to ensure the handling of POST request only
    if request.method == "POST":
        #store the form value
        user_name = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        
        # store the user details in the user database table
        user = User(username = user_name, user_email = email, user_password = password)
        
        # add the user object to the database
        db.session.add(user)
        
        # commit changes to the database 
        db.session.commit()
        
        return 'User registration successful'
    return render_template('register.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)