# Modules/blueprints
from .dashboard import dashboard


class RQDashboard(object):
    def __init__(self, app=None, url_prefix='/rq', auth_handler=None):
        self.url_prefix = url_prefix
        if app is not None:
            self.app = app
            self.init_app(app)
        else:
            self.app = None
        self.app.auth_handler = auth_handler

    def init_app(self, app):
        """Initializes the RQ-Dashboard for the specified application."""
        app.register_blueprint(dashboard, url_prefix=self.url_prefix)
        app.config['rq_url_prefix'] = self.url_prefix
