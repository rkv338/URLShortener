# URLShortener
Simple URL shortener

Uses CRC32 hashing of URLs fed into the API.

Stores the hash as a key pointing to the URL as the value.

Mappings are stored in a DynamoDB table for its lack of rigid schema.

However, since we only need to store the hash and its respective URL, this could have also been done in an RDS SQL DB.
