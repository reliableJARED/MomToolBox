#http://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
#http://flask-socketio.readthedocs.org/en/latest/
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO
from flask.ext.socketio import emit, send
import time
import json
import random
import threading
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

global coinCount
 
def get_url(url):
	r = requests.get(url)
	#print r.text
	soup = BeautifulSoup(r.content)
	#print soup
	ingrd = soup.find_all(attrs={'itemprop':'ingredients'})
	print ingrd
	ingredientHolder = []
	for i in ingrd:
		print i.text
		ingredientHolder.append(i.text)
	return {'ingrd':ingredientHolder}

@app.route('/')
def index():
    return render_template('shoplist.html')

@socketio.on('connect', namespace='/')
def test_connect():
    print "new connection"

@socketio.on('disconnect', namespace='/')
def test_disconnect():
    print 'user disconnected'

@socketio.on('message')
def handle_message(data):
	dataIN = json.loads(data)
	print dataIN
	if dataIN.iterkeys().next() == "url":
		site = get_url(dataIN["url"])
		emit('message',json.dumps(site))
	
@socketio.on('custom')
def handle_custom(data):	
	emit('message',json.dumps(data),broadcast=True)
  
if __name__ == '__main__':
    #CHANGE HOST
    ip = raw_input("Enter host ip to use: ")
    socketio.run(app,host=ip,port=8000)
