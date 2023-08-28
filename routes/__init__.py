from .zone import *
from .grade import *
from .fund_request import *
from .user import *
from .activity_domain import *

# Register the blueprints
def register_routes(app):
    app.register_blueprint(zone_bp)
    app.register_blueprint(grade_bp)
    app.register_blueprint(fund_request_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(activity_domain_bp)


# This line allows you to import `register_routes` from `app.routes` in app.py
__all__ = ["register_routes"]
