#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
<form>
    <input name ="q">
    <input type ="submit">
</form>

import webapp2

form="""
<form action ="/Signup">
    <input name ="q">
    <input type ="submit">
</form>
"""

#class MainHandler(webapp2.RequestHandler):
#    def get(self):
#        self.response.write('Heeeeello world!')

#app = webapp2.WSGIApplication([
#    ('/', MainHandler)
#], debug=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

class Signup(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

    def post(self):
        have_error = False
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

#class Welcome(BaseHandler):

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/unit2/signup' Signup)
#    ('/unit/welcome', Welcome)
], debug=True)
