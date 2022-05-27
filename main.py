import requests
from bs4 import BeautifulSoup
import smtplib
import ssl
from email.message import EmailMessage

request_link = requests.get('https://www.1stdibs.com/creators/le-corbusier/furniture/')
request_link2 = request_link.text

# going with request_link.text
# link_content = request_link.content

soup = BeautifulSoup(request_link2, 'html.parser')
all_h2 = soup.find_all('h2')
all_div = soup.find_all('div')
all_img = soup.findAll('img')

# output to a separate file after run, good for keeping track of available items
"""
with open('output_divs.txt', 'w') as f:
    for link in all_div:
        f.write(str(link))
        f.write('\n')
        f.write('\n')

with open('output_piece_names.txt', 'w') as f:
    for link in all_h2:
        f.write(str(link))
        f.write('\n')
        f.write('\n')

with open('output_images.txt', 'w') as f:
    for link in all_img:
        f.write(str(link))
        f.write('\n')
        f.write('\n')
"""

subject = "Here are your chairs"
body = str(all_img)
sender = 'YOUR EMAIL'
receiver = "THEIR EMAIL"

# this will prompt you for a password, i feel this is better than hardcoding
password = input("enter your password!")

message = EmailMessage()
message["From"] = sender
message["To"] = receiver
message["Subject"] = subject
# message.set_content(body)

html = f"""
<html>
    <body>
    <h1>{subject}</h1>
    <img src={all_img}/>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending . . ")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())

print("Sent!")