from auth.boto import getTable


hashTable = getTable()

def pushHash(hash, long_url, timestamp=''):
    item = {
        'hash': hash,  
        'long_url': long_url,
        'timestamp': timestamp
    }

    try:
        hashTable.put_item(Item=item)
        print('Item successfully inserted')
    except Exception as e:
        raise Exception('Could not push to DB', hash)
