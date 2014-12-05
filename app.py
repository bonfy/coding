#-*-coding:utf-8-*-

import bottle
from bottle import Bottle
from bottle import route, run, template,Bottle, debug, template,request,redirect,response,error,hook
from bottle import static_file


app = Bottle()

@app.route('/')
@app.route('/index')
def index():
    return 'hello world'

###################
#
# Develop
#
###################

bottle.debug(True)
run(app=app,host='localhost',port=8888,reloader=True,debug=True)

###################
#
# Production
#
###################

#run(app=sessionApp,host='localhost',port=8888)#,reloader=True,debug=True)
