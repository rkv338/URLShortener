import base62

def generateHash(longUrl):
    return base62.encode(longUrl)