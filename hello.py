#!/usr/bin/env python
import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write('<html><body>hello</body></html>')

app = webapp2.WSGIApplication([
  ('/', MainPage),
], debug=True)
