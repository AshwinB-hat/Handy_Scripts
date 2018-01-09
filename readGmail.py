import imaplib
import sys
def read(userName,password):
	name = userName
	imap = imaplib.IMAP4_SSL("imap.gmail.com",993)
	imap.login(userName,password)
	imap.select('INBOX')
	status,response = imap.search(None, "Unseen")
	# unread = response[0]
	for msg in response[0].decode('utf-8').split(' '):
		imap.uid('STORE', msg, '+FLAGS', '\SEEN')
		print(msg)
	#print(response)
if __name__=="__main__":
	if(len(sys.argv)<3):
		print("[Username] [password]")
	else:
		read(sys.argv[1],sys.argv[2])