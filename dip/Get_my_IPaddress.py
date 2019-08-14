import socket
import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = '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'
#API_KEY format is 'XX.xxxxxxx~~-xxxxxxxxxxxxx'
sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, IP):
    from_email = Email("wntjdals2012@gmail.com")
    #If you enter the wrong email, a compilation error will occur.
    to_email = Email(email)
    subject = "Raspberry Pi's IP information"
    content = Content("text/plain","Raspberry Pi's IP is " + IP )
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

if __name__ == '__main__':
    print('Func_called - main')
    My_IP = socket.gethostbyname(socket.gethostname())
    print("My local ip is " + My_IP)
    send_email('wntjdals2015@naver.com', My_IP )
    print("complete")
else:
    print('Func_called - imported')
    
