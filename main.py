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

table_head = """
    <table>
        <tbody>
"""

table_foot = """
        </tbody>
    </table>
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
                                <input type="text" name="username" value required/>
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

#class Signup(webapp2.RequestHandler):
#    def get(self):
#        self.response.out.write(form)
#
#    def post(self):
#        have_error = False
#        username = self.request.get('username')
#        password = self.request.get('password')
#        verify = self.request.get('verify')
#        email = self.request.get('email')

#class Welcome(BaseHandler):

app = webapp2.WSGIApplication([
    ('/', MainPage)
#    ('/name' username)
#    ('/password', password)
], debug=True)
