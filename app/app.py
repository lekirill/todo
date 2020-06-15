import os

import routes
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI'] if 'SQLALCHEMY_DATABASE_URI' in os.environ \
    else None
db = SQLAlchemy(app)
migrate = Migrate(app, db)
logger = logging.getLogger('app start')

if __name__ == '__main__':
    routes.setup_app(app)
    db.create_all()
    app.run(host='0.0.0.0', port=os.environ['PORT'], debug=False)
