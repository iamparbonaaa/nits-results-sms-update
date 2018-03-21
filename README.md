# nits-results-sms-update

DESCRIPTION:
This is a Python application to notify me when the semester results get posted on my college website. The script, when run, scrapes the website,
and when it encounters the string "Results", it sends an SMS to my mobile number to notify me.
Web scraping is done with the help of the bs4 module, and SMS is sent via Twilio.

PRE-REQUISITES:
1. Pyhton 3.x
2. Twilio API and account

USAGE:
1. Create a Twilio account, and get the Twilio API. Refer to https://www.twilio.com/docs/api/messaging/send-messages for reference.
2. Change the URL passed to requests.get().
3. Change the Twilio login id and password.
4. Change the argument passed to bs4.select() so that it matches the formatting of the website you are scraping.
5. Run the script in a Python 3.x environment
