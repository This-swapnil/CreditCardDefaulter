from flask import Flask, request, render_template
from flask import Response
from flask_cors import CORS, cross_origin

from training_Validation_Insertion import train_validation

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train", methods=['POST'])
@cross_origin()
def trainRouteClient():
    try:
        if request.json["filepath"] is not None:
            path = request.json["filepath"]
            train_valObj = train_validation(path)  # object initialization
            train_valObj.train_validation()  # calling the train_validation function
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)
    return Response("Training Successfull!!")


if __name__ == "__main__":
    app.run(debug=True)
