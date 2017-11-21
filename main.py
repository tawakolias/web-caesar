from flask import Flask, request, redirect
from caesar import rotate_string
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/web" method="post">
      <label> Rotate: <input type = "text" name="rotate">
      </label>
  <textarea name="message" >{0}</textarea>
  <br>
  <input type="submit">
</form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')


@app.route("/web", methods=['POST'])
def encryption():
    rot = int(request.form['rotate'])
    char = request.form['message']
    
    abc =  rotate_string(char, rot)
    return form.format(abc)



app.run()