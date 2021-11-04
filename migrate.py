from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:211218@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = '571ebf8e13ca209536c29be68d435c00'

db = SQLAlchemy(app)
migrate = Migrate(app, db)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

    