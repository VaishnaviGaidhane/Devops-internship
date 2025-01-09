from flask import Flask
helloflask = Flask(__name__)
@helloflask.route("/")
def run():
    return"{\"message\":\"Hello Flask!\"}"
if __name__=="__main__":
    helloflask.run(host="0.0.0.0", port=int("5000"), debug=True)
    