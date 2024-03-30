from flask import Flask
from views import views, host, port
import os
import sys

dir = os.getcwd()
sys.path.append(dir)
print(dir)


app = Flask(__name__,template_folder=f'{dir}/templates')
app.register_blueprint(views, url_prefix = "/")


if (__name__) == "__main__":
    app.run(debug=True)

