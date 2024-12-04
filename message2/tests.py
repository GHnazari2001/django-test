from django.test import TestCase
from django.test import Client

# Create your tests here.
class MessageTest(TestCase):

    def url_exist(self):
        response= self.client.get("/message2/")
        self.assertEqual(response.status_code,200)
    
   # def test_url_exist(self):
      # client= Client()
       # response= client.get('/message2/')
        #self.assertEqual(response.status_code,200)    

