import smtplib
from email.mime.multipart   import MIMEMultipart
from email.mime.text        import MIMEText

class Email():

    #Must change this parameters
    SENDER      = 'xxxxxxx'
    SMTP        = 'xxxxxxx'
    USER_LOGIN  = 'xxxxxxx'
    USER_PSW    = 'xxxxxxx'
    
    SUBJECT     = 'A Invitation for you'
    
    mail = '''
        Dear {firstname} {lastname}
        we are so glad to invite you to next party saturday night

        See you there

        R.
        '''

    def format_mail(self, first_name, last_name):
        #format mail with last_name and first_name
        self.mail_formatted = Email.mail.format(
           firstname    = first_name,
            lastname    = last_name)

    def send_mail(self, list_mails):
        #connect to server SMTP before sending mails
        server = smtplib.SMTP(Email.SMTP)
        server.login(Email.USER_LOGIN, Email.USER_PSW)

        print('OK')
        outer               = MIMEMultipart()
        outer['Subject']    = Email.SUBJECT
        outer['From']       = Email.SENDER

        for contact in list_mails:
            #check is contact object has to receive the invitation 
            if(contact.to_send):
                self.format_mail(contact.firstname, contact.lastname)
                outer.attach(MIMEText(self.mail_formatted, 'plain'))
                print('Start to send mail ---> ' + contact.mail + '.....')
                #Mail object created. Send it
                server.sendmail(Email.SENDER, contact.mail, outer.as_string())
                print('OK')
        #Quit from the mail server    
        server.quit()
        
class Contact():

    def __init__(self, firstname, lastname, mail, to_send):
        self.firstname  = firstname
        self.lastname   = lastname
        self.mail       = mail
        self.to_send    = to_send

