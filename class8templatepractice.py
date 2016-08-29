import os
import cgi
import jinja2
import webapp2

#create jinja environment
templates_path = os.path.join(
        os.path.basename(__file__), 'templates')

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(
                                template_path),autoescape = True)

#this is supposed to be walkthrough7 from flicklist-python but I can't find it
#keep doctype portion
class Index(webapp2.RequestHandler):
    def get(self):
        movies=getCurrentWatchList()
        jinja_env.get_template("class8tempracticeedithtml.py")#should be file ending in .html
        response = template.render(movies = movies)

        self.response.write(response)
#in each of these files, there is an app.yaml file
class AddMovies(webapp2.RequestHandler):
