import invitation
import requests

#Change URL 
REQUEST_URL = 'INSERT URL TO YOUR SERVICE'

def get_list_mail_from_server ():
    response = requests.get(REQUEST_URL)
    print('Try to get list.........')
    if(response.status_code == 200):
        print('OK')
        return response
    else :
        print('KO!!')
    return None



def create_contact_list(json_obj):
    contacts_list = []
    for contact in json_obj:
        contact = invitation.Contact(
            contact['firstname'],
            contact['lastname'],
            contact['mail'],
            contact['to_send'])
        contacts_list.append(contact)
    return contacts_list


def main():
    #get list of contact from the server
    response = get_list_mail_from_server()
    if(response is not None):
        print(response.text)
        #create a list with Contact obj
        contacts_list = create_contact_list(response.json())
        print('Connetion to send mail.......')
        email = invitation.Email()
        #Send mail 
        email.send_mail(contacts_list)
    else :
        print('Error to get mail list')

main()        
    
