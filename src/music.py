import flask, flask.views
import os
import utils

class Music(flask.views.MethodView):
    @utils.login_required
    def get(self):
        
		
		
        return flask.render_template("music.html",)
    