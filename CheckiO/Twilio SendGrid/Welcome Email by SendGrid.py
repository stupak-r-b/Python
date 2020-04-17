"""
    Your mission is to create a function that sends a welcome email to a user. The function gets two arguments: email and the name of the user.
Subject of the email should be "Welcome" and body simply "Hi {name}" ({name} should be replaced by a user's name)

Input: Two arguments: email and a username.
Output: None. You should send an email. You don’t need to return anything.
"""
import sendgrid
from sendgrid.helpers.mail import Mail, SendGridException


def send_email(email, name):

    BODY = f'Hi {name}'; SUBJECT = 'Welcome'
    sg = sendgrid.SendGridAPIClient("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")
    message = Mail(from_email='test@example.com', to_emails=email, subject=SUBJECT, plain_text_content=BODY.format(name))
    try:
        response = sg.send(message)
    except SendGridException as e:
        print(str(e))


if __name__ == '__main__':

    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
