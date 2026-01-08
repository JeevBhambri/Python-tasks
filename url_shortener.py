from flask import Flask, redirect, request, jsonify
import hashlib

app = Flask(__name__)

url_to_code = {}
code_to_url = {}

@app.route("/")
def home():
    return "URL Shortener is running"

@app.route("/shorten", methods=["POST"])
def shorten():
    long_url = request.json.get("url")

    if long_url in url_to_code:
        return jsonify({"short_code": url_to_code[long_url]})

    short_code = hashlib.md5(long_url.encode()).hexdigest()[:6]

    original_code = short_code
    counter = 1
    while short_code in code_to_url:
        short_code = original_code + str(counter)
        counter += 1

    url_to_code[long_url] = short_code
    code_to_url[short_code] = long_url

    return jsonify({"short_code": short_code})

@app.route("/<short_code>")
def redirect_url(short_code):
    long_url = code_to_url.get(short_code)
    if long_url:
        return redirect(long_url)
    return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)




'''
Use this command on cmd to make the short URL:

curl -X POST http://127.0.0.1:5000/shorten ^
     -H "Content-Type: application/json" ^
     -d "{\"url\":\"https://www.google.com\"}"

'''