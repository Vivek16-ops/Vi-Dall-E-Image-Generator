from flask import Flask, jsonify, request, render_template
from waitress import serve
from openai import OpenAI
from api_key import key


app = Flask(__name__)

open_api_key = key
client = OpenAI(api_key=open_api_key)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/imageGeneration", methods=["POST"])
def imageGeneration():

    # Receive data from the body of the fetch request
    data = request.json

    response = client.images.generate(
      model="dall-e-3",
      prompt=data,
      size="1024x1024",
      quality="standard",
      n=1,
    )
    image_url = response.data[0].url
    return jsonify({"img_url":image_url})


if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=5000)


# url:-  http://127.0.0.1:5000
