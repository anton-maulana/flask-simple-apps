import os
import  sys

moddir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
sys.path.append(moddir)

from fraud_detection import  create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host=app.config["HOST"], port=app.config["PORT"])