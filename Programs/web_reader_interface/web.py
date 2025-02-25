import ssl
from urllib import request
from urllib.error import URLError, HTTPError

def leer(url):
    context = ssl._create_unverified_context()
    
    try:
        with request.urlopen(url, context=context) as file:
            for line in file:
                print(line.decode('utf-8'))
    except URLError as e:
        return f'Error accessing the URL {url}: {e}'

# Call the function
leer('https://www.purina.es/encuentra-mascota/razas-de-gato')