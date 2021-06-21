
import webapp2
import jinja2
from user import User
from google.appengine.api import users
from google.appengine.ext import ndb
from anagramengine import Anagram
from add import addAnagram
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)


def sort(n):
   ordered = ''.join(sorted(n))
   return ordered



class MainPage(webapp2.RequestHandler):
    def get(self):
        currentuser = users.get_current_user()

        if currentuser == None:
            template_values = {
                'login_url': users.create_login_url(self.request.uri)
            }
            template = JINJA_ENVIRONMENT.get_template('main_guest.html')
            self.response.write(template.render(template_values))
            return

        myuser_key = ndb.Key('User', currentuser.user_id())
        myuser = myuser_key.get()
        if myuser == None:
            myuser = User(id=currentuser.user_id())
            myuser.put()


        template_values = {
            'logout_url' : users.create_logout_url(self.request.uri),
            'running':'running',
            'user':currentuser

        }
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template.render(template_values))


    def post(self):
        self.response.headers['Content - Type'] = 'text / html'
        action = self.request.get('button')
        if action == 'Check':
            word = self.request.get('word')

            sortedword = sort(word)
            currentuser = users.get_current_user()
            key = currentuser.user_id() + sortedword

            lex = ndb.Key(Anagram, key)
            retrieveWord = lex.get()

            if retrieveWord == None:
                self.redirect('/')

            else:
                template_values = {
                    'query':retrieveWord.word,
                    'count':str(len(retrieveWord.word)),
                    'lex': str(len(sortedword))

                }
                template = JINJA_ENVIRONMENT.get_template('main.html')
                self.response.write(template.render(template_values))





app = webapp2.WSGIApplication([
    ('/' , MainPage),
    ('/addAnagram',addAnagram)
    ], debug=True)
