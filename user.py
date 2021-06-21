from google.appengine.ext import ndb
from anagramengine import Anagram

class User(ndb.Model):
    username = ndb.StringProperty()
