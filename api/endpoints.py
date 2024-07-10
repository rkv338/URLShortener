from flask import Flask, jsonify, redirect, request
from hashGen import generateHash
app = Flask(__name__)

@app.post('/shorten') 
def shorten():
   # logic to shorten URL
   req = request.get_json()
   long_url = req.get('long_url')
   # validate that the url is actually a URL
   hash = generateHash(long_url)

   if not long_url:
      return jsonify({'error': 'No URL provided'}), 400

   return hash

@app.get('/<shortURL>')
def getLongURL(shortURL):
   # logic to fetch long url of this short url
   return redirect("https://www.google.com", code=301)