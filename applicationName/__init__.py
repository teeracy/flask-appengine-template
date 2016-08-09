from flask import Flask

app = Flask(__name__)
app.secret_key = "somesecretkeyherepleasechange" # CUSTOMIZE
app.static_folder = '../static'
app.template_folder = '../templates'

import clientRoutes