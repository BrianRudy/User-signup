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

import webapp2
import re
import cgi

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
    <h1>
        Signup
    </h1>
<body>
"""

page_footer = """
</body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):

#        edit_header = "<h1>Signup</h1>"

        add_name = """
        <form action="/name" method="post">
            <table>
                    <tr>
                        <td><label>Username</label></td>
                        <td>
                            <input type="text" name="username" value="" />
                        </td>
                    </tr>
        </form>
        """

        add_password = """
                    <tr>
                        <td><label>Password</label></td>
                        <td><input type="text" name="password" /></td>
                    </tr>
            </table>
            <input type ="submit"/>

        </form>
        """

#        verify_password = """
#                    <tr>
#                        <td><label>Verify Password</label></td>
#                        <td><input type="text" name="verify" required/></td>
#                    </tr>
#        </form>
#        """

#        add_email = """
#                    <tr>
#                        <td><label>Email (optional)</label></td>
#                        <td><input type="text" name="email" value=""/></td>
#                    </tr>
#            </table>
#            <input type ="submit"/>
#        </form>
#        """

        error = self.request.get("error")
        error_element = "<p class='error'>" + error + "</p>" if error else ""

#        main_content = add_name + add_password + verify_password + add_email + error_element
        main_content = add_name + add_password + error_element
        content = page_header + main_content + page_footer
        self.response.write(content)

class Username(webapp2.RequestHandler):
    def post(self):
        user_name = self.request.get("username")
        pass_word = self.request.get("password")

        if (user_name) == "" or (user_name.strip() == ""):
            error = "That's not a valid username".format(user_name)
            error_escaped = cgi.escape(error, quote=True)

            self.redirect("/?error=" + error_escaped)

#        if USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
#            def valid_username(username):
#                return USER_RE.match(username)

        username_escape = cgi.escape(user_name, quote=True)

        username_element = username_escape
        sentence = "Welcome " + username_element
        content = page_header + sentence
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/name', Username)
#    ('/password', password)
], debug=True)
