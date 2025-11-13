import random
import string

class Codec:

    def __init__(self):
        self.url_map = {}
        self.base = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        # Generate a random 6-character key
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        # Ensure uniqueness
        while code in self.url_map:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.url_map[code] = longUrl
        return self.base + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        # Extract the code after the last '/'
        code = shortUrl.split('/')[-1]
        return self.url_map.get(code, "")
