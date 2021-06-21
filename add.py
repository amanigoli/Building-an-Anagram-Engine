import os
import webapp2
import jinja2
from user import User
from google.appengine.api import users
from google.appengine.ext import ndb
from anagramengine import Anagram


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)
def sort(n):
    listWord = list(n)
    ordered = ''.join(sorted(listWord))
    return ordered

class addAnagram(webapp2.RequestHandler):

    def get(self):


          currentuser = users.get_current_user()
          if currentuser == None:
              template_values = {
                  'login_url': users.create_login_url(self.request.uri)
              }
              template = JINJA_ENVIRONMENT.get_template('main_guest.html')
              self.response.write(template.render(template_values))
              return

          template_values = {

                'logout_url': users.create_logout_url(self.request.uri),
                'running':"running"
            }
          template = JINJA_ENVIRONMENT.get_template('addAnagram.html')
          self.response.write(template.render(template_values))


    def post(self):

        self.response.headers['Content - Type'] = 'text / html'
        action = self.request.get('button')

        if action == 'ADD WORD':
            words = self.request.get('word')
            WordLength = len(words)
            sortedword = sort(words)

            if words == '':
                self.redirect('/')
            else:


                currentuser = users.get_current_user()
                key = currentuser.user_id()+sortedword

                lex = ndb.Key(Anagram, key)
                retrieveWord = lex.get()

                if retrieveWord == None:
                    wordInfo = Anagram(id=key,sortedword=sortedword.lower(),wordLength=WordLength,email=currentuser,wordCount=1)
                    wordInfo.word.append(words)
                    wordInfo.put()
                    self.redirect('/')

                else:
                    counter=len(retrieveWord.word)+1
                    retrieveWord.wordCount=counter
                    retrieveWord.word.append(words)
                    retrieveWord.put()
                    responseMessage={
                        "message": "New dictionary has been added to the datastore successfully. "
                    }
                    template = JINJA_ENVIRONMENT.get_template('addAnagram.html')
                    self.response.write(template.render(responseMessage))
