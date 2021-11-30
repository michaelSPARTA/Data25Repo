from pprint import pprint
import requests

requests_bbc = requests.get('https://www.bbc.co.uk/')

pprint(requests_bbc.content)
