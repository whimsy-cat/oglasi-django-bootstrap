import requests
from oglasi_app import settings

def send_mailgun_mail(to_mail, to_full_name, subject, template, data):
    url = "https://api.eu.mailgun.net/v3/moj-dom.me/messages"
    mailgun_data = {
        "from": "Moj Dom <podrska@moj-dom.me>",
        "to": f"{to_full_name} <{to_mail}>",
        "subject": subject,
        "template": template,
        "h:X-Mailgun-Variables": data,
    }
    response = requests.post(url, auth=("api", settings.MAILGUN_API_KEY), data=mailgun_data)
    return response