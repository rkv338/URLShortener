from flask import Flask, jsonify, redirect, request
import binascii
from datetime import datetime, timezone
from db_actions.push import pushHash
from db_actions.pull import pullLongUrl
app = Flask(__name__)


def createHash(long_url):
   url_bytes = bytes(long_url, 'utf-8')

   return binascii.crc32(url_bytes)


@app.post('/shorten') 
def shorten():
   # logic to shorten URL
   req = request.get_json()
   long_url = req.get('long_url')
   if not long_url or long_url == '':
      return jsonify({'error': 'No URL provided'}), 400
   # validate that the url is actually a URL
   hash = createHash(long_url)
   # if hash in __mappings:
   #    hash = createHash(datetime.now(timezone.utc) + long_url)
   s_hash = str(hash)
   try:
      pushHash(s_hash, long_url)
   except Exception as e:
      return jsonify({'error': e}), 400
   
   return 'http://localhost:5000/' + s_hash, 200


@app.get('/<hash>')
def getLongURL(hash):
   try:
      long_url = pullLongUrl(hash)
   except Exception as e:
      return jsonify({'error': e}), 400
   return redirect(long_url, code=301)

