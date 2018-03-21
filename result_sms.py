from twilio.rest import Client
import bs4, requests

account = 'xxxxxxxxxxx'
pwd = 'xxxxxxxxxxx'
myCell = '+0000000000'
twlNum = '+00000000000'
twilioCli = Client(account, pwd)
res = requests.get('http://nits.ac.in')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
elems = soup.select('div > a > b')
if 'Results' in str(elems):
    twilioCli.messages.create(body='Your semester results may be out', from_=twlNum, to=myCell)
