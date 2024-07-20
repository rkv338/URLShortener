
from auth.boto import getTable


hashTable = getTable()

def pullLongUrl(hash):
    key = {
        'hash': hash
    }

    long_url = None
    try:
    
        response = hashTable.get_item(Key=key)

        if 'Item' in response:
            long_url = response['Item']['long_url']
            print('Item fetched successfully:', long_url)
        else:
            raise Exception('Item not found')
    except Exception as e:
        raise Exception('Could not pull hash from DB: ', hash)

    return long_url