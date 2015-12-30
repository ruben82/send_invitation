# send_invitation

Python

Make a request and return a list of contact. Send a mail to the contact you have TO_SEND attribute set to true


README


This project was create to send invitation mail to some people from a contact list

The steps needed to carry out this program are:

1) Install Python to your environment  http://www.python.it/download/ 
    Python 2.10 is used to develop this project

2) Install “Request” library  http://docs.python-requests.org/en/latest/user/install/

3) Fill field in invitation.py file
   	SENDER      	=  ‘sender mail
    	SMTP          	=  ‘your smtp’	
    	USER_LOGIN  =  ‘mail login’
    	USER_PSW     =  ‘mail password’

4) In send_invitation.py  you must change REQUEST_URL with your service url. Must return a JSON object whit this model.
	
	[{"firstname”:”NAME”,”lastname”:”LAST_NAME”,”mail”:”MAIL”,”to_send":true}]
	
	 You can use email.php as example or edit it. 


5) You can open send_invitation.py from IDLE or write python {PATH_TO_PROJECT}/send_invitation.py in command shell to  run it 


for support feel free to write me at info@rubenroccodeluca.it
