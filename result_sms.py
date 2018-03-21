from twilio.rest import Client
import bs4, requests

account = 'AC7ea308c25e5a2505d48759932cbb35d7'
pwd = 'f36b3268ea4de308d4a67c2dc0a3b10f'
myCell = '+917086504992'
twlNum = '+17748543092'
twilioCli = Client(account, pwd)
res = requests.get('http://nits.ac.in')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('div > a > b')
if 'Results' in str(elems):
    twilioCli.messages.create(body='Your semester results may be out', from_=twlNum, to=myCell)
