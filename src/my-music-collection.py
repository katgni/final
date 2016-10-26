import flask
from flask import Flask, g, redirect, url_for, render_template, request, jsonify, json, url_for
import sqlite3
import settings

from main import Main
from login import Login
from music import Music  

app = Flask(__name__)

db_location = 'var/mydatabase.db'
app.secret_key = settings.secret_key

# database config
def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
    return db
	
@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db() 
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()	
	
# Routes for templates
@app.route("/")
def root():
  return render_template('navbar_root.html') 

@app.route("/albums/")
def page1():
  return render_template('navbar_albums.html')

@app.route("/artists/")
def page2():
  return render_template('navbar_artists.html')

@app.route("/genre/")
def page3():
  return render_template('navbar_genre.html')
  
# To see all records in database 
@app.route("/database/")
def page4():
    db = get_db()
    

    page = []
    page.append('<html><ul>')
    sql = "SELECT rowid, * FROM albums ORDER BY id"
    for row in db.cursor().execute(sql):
        page.append('<li>')
        page.append(str(row))
        page.append('</li>')
		


    page.append('</ul><html>')
    return ''.join(page)
	
	
# Routes for login
app.add_url_rule('/',
                 view_func=Main.as_view('main'),
                 methods=["GET"])
app.add_url_rule('/<page>/',
                 view_func=Main.as_view('page'),
                 methods=["GET"])
app.add_url_rule('/login/',
                 view_func=Login.as_view('login'),
                 methods=["GET", "POST"])

app.add_url_rule('/music/',
                 view_func=Music.as_view('music'),
                 methods=['GET'])

@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404
	
	
# All albums route	
@app.route('/allalbums/')
def page5():
    json_data=open('static/albums.json').read()
    albums= json.loads(json_data)
    return render_template("albums.html", results=albums)	
	
# Single albums route	
@app.route('/<artist_name>/<album_name>/')
def page6(album_name, artist_name):
    json_data=open('static/albums.json').read()
    albums= json.loads(json_data)
    json_data=open('static/tracks.json').read()
    tracks= json.loads(json_data)
    return render_template("album.html", albums=albums, album_name=album_name, artist_name=artist_name, tracks=tracks)



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
