page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>User Signup</title>
            <style>
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

import webapp2
import re
import cgi

form ="""
<form method="post"
    <h1>User Signup</h1>
    <table>
        <tr>
        <td>User Name</td>
        <td><input name="user_name" type="text" value="%(user_name)s"</td>
        <td><div style="color:red">%(error_user_name)s</div></td>
        </tr>

        <tr>
        <td>Password</td>
        <td><input name="password" type="password" value=""></td>
        <td><div style="color:red">%(error_password)s</div></td>
        </tr>

        <tr>
        <td>Verify Password</td>
        <td><input name="verify_password" type="password" value=""</td>
        </tr>

        <tr>
        <td>Email (optional)</td>
        <td><input name="email" type="text" value="%(email)s"</td>
        <td><div style="color:red">%(error_email)s</div></td>
        </tr>
    </table>

        </td><input type="submit"></td></tr>
</form>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_user_name(user_name):
    return user_name and USER_RE.match(user_name)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def write_form(self, user_name="", error_user_name="", error_password="", email="", error_email=""):
        self.response.out.write(form % {"user_name": user_name,
                                        "error_user_name": error_user_name,
                                        "error_password": error_password,
                                        "email": email,
                                        "error_email": error_email
                                        })

    def get(self):
        self.write_form()

    def post(self):
        have_error = False
        q_user_name = self.request.get('user_name')
        q_password = self.request.get('password')
        q_verify_password = self.request.get('verify_password')
        q_email = self.request.get('email')

        user_name = q_user_name
        password = q_password
        verify_password = q_verify_password
        email = q_email

        if not valid_user_name(user_name):
            error_user_name = "That is not a valid username."
            have_error = True
        else:
            error_user_name = ""

        if not valid_password(password):
            error_password = "That is not a valid password."
            have_error = True
        elif q_password != q_verify_password:
            error_password = "Your passwords do not match."
            have_error = True
        else:
            error_password = ""

        if not valid_email(email):
            error_email = "That's not a valid email."
            have_error = True
        else:
            error_email = ""

        if have_error:
            self.write_form(q_user_name, error_user_name, error_password, q_email, error_email)
        else:
            self.redirect("/welcome?user_name=" + user_name)

class Welcome(webapp2.RequestHandler):
    def get(self):
        user_name = self.request.get('user_name')

        if valid_user_name(user_name):
            user_name_escape = cgi.escape(user_name, quote=True)
            user_name_element = user_name_escape
            sentence = "Welcome, " + user_name_element + "!"
            content = page_header + sentence + page_footer
            self.response.write(content)
        else:
            self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
