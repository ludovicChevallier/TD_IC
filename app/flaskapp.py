from flask import Flask
from redis import Redis,RedisError
import socket

redis =Redis(host="redis-server",db=0)

app=Flask(__name__)

@app.route('/')
def index():
    return "<h1> Bienvenue sur mon site </h1>"
    
@app.route('/visit')
def counter_incr():
    try:
        visits=redis.incr("couter")
    except:
        visits="<i> je n'ai pas resussi à me connecter sur redis </i>"
    html="<h1> Nombre de visite {} </h1>".format(visits)
    return html
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port =80)
