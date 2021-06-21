from google.appengine.ext import ndb


class Anagram(ndb.Model):
    word = ndb.StringProperty(repeated=True)
    sortedword = ndb.StringProperty()
    wordCount=ndb.IntegerProperty()
    wordLength = ndb.IntegerProperty()
    email=ndb.UserProperty()
