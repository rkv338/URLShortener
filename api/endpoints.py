from flask import Flask, jsonify, request
app = Flask(__name__)

@app.post('/shorten') 
def shorten():
   # logic to shorten URL
   req = request.get_json()
   long_url = req.get('long_url')

   if not long_url:
      return jsonify({'error': 'No URL provided'}), 400

   return long_url

@app.get('/longURL/<shortURL>')
def getLongURL(shortURL):
   # logic to fetch long url of this short url
   return "https://www.google.com"