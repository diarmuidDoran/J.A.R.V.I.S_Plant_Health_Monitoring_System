# main.py
import os
from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

# from flask_migrate import Migrate
from blueprints.config import postgresConn
from blueprints.documented_endpoints import blueprint as documented_endpoint

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = postgresConn
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
jarvis_db = SQLAlchemy(app)
jarvis_db.init_app(app)

# migrate = Migrate(app.py, jarvis_db)
app.register_blueprint(documented_endpoint)

if __name__ == "__main__":
    # print(os.environ["DATABASE_CONNECTION"])
    app.run(debug=True)  # TODO remove before hand in
