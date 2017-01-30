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
<body>
"""

page_footer = """
</body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):

        edit_header = "<h1>Signup</h1>"

        add_name = """
        <form action="/name" method="post">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label>
                                Username
                            </label>
                        </td>
                        <td>
                            <label>
                                <input type="text" name="username" value="username"/>
                            </label>
                        </td>
                    </tr>
        </form>
        """

        add_password = """
        <form action="/password" method="post">
                    <tr>
                        <td>
                            <label>
                                Password
                            </label>
                        </td>
                        <td>
                            <label>
                                <input type="text" name="password"/>
                            </label>
                        </td>
                    </tr>
        </form>
        """

        verify_password = """
        <form action="/verify" method="post">
                    <tr>
                        <td>
                            <label>
                                Verify Password
                            </label>
                        </td>
                        <td>
                            <label>
                                <input type="text" name="verify"/>
                            </label>
                        </td>
                    </tr>
        </form>
        """

        add_email = """
        <form action="/email" method="post">
                    <tr>
                        <td>
                            <label>
                                Email (optional)
                            </label>
                        </td>
                        <td>
                            <label>
                                <input type="text" name="password"/>
                            </label>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type ="submit"/>
        </form>
        """

        main_content = edit_header + add_name + add_password + verify_password + add_email
        content = page_header + main_content + page_footer
        self.response.write(content)

class username(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")

        if username == "" or (username.strip() ==""):
            error = "That's not a valid username"
            error_escaped = cgi.escape(error, quote=True)

            self.redirect("/?error=" + error_escaped)

        if USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
            def valid_username(username):
                return USER_RE.match(username)

#class Welcome(BaseHandler):

app = webapp2.WSGIApplication([
    ('/', MainPage)
    ('/name' username)
#    ('/password', password)
], debug=True)
