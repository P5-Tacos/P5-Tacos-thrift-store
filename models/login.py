from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models.module import UserTT, db
from app import app

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user_all(user_id):
    return UserTT.query.get(int(user_id))

def model_logout_all():
    logout_user()