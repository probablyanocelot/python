import requests

from bs4 import BeautifulSoup
# Send the mail
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime as dt


now = dt.now()

# email content placeholder

content = ''

#extracting Hacker News Stories

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('<b>HN Top STORIES:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i,tag in enumerate(soup.find_all('td', attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text!='More' else '')
        #print(tag.prettify) #find all ('span',attrs={'class':'sitestr'}))
    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>---------<br>')
content +=('<br><br>End of Message')

#sending the email
print('Composing Email')
