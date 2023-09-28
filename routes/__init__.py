from .zone import *
from .grade import *
from .fund_request import *
from .user import *
from .activity_domain import *
from .employee import *
from .cost_center import *
from .level import *

# Register the blueprints
def register_routes(app):
    app.register_blueprint(zone_bp)
    app.register_blueprint(grade_bp)
    app.register_blueprint(fund_request_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(activity_domain_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(cost_center_bp)
    app.register_blueprint(level_bp)
