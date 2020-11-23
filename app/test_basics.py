import os 
import unittest
# on import l'objet app du fichier flaskapp
from flaskapp import app

from redis import Redis
#permet de runer des testes
class CounterTest(unittest.TestCase):

    def setUp(self):
        
        self.app=app.test_client()

    def tearDown(self):
        pass
    #definir mes testes
    #teste1
    def test_welcome_page(self):
        #make a get request, on endpoint '/
        reponse =self.app.get("/")
        # si sa marche le site retroune 200
        self.assertEqual(reponse.status_code,200)

    #teste2
    def test_redis_connection(self):
        redis=Redis(host="redis-server",db=0)
        self.app.get('/visit')
        #on regarde bien que le conter passe à 1 quand on se co dessus
        self.assertEqual(int(redis.get("counter")),1)
if __name__=='main':
    unittest.main()