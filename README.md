# EmailTemplate
Allows a user to create an email template and send it to multiple people.

First let me say this code was initially designed around: http://naelshiab.com/tutorial-send-email-python/ . This program was created because I needed to send personalized emails to multiple people.  Each email needed to have different names in the email.  I am putting this code out there because it may be useful to someone.  This means use it at your own peril.  I am not responsible for anything that happens with you using this code.  

I have provided two example files that will help you use this code: message.txt and recipients.csv.  The message.txt file is the email you wish to send to others.  The templated names like from_first_name will be replaced with the person that will be receiving the email.  The recipients.csv file is the list of people you wish to send an email.  You will need to add some real emails for this code to properly function.

This code should work for Gmail accounts, but I haven't really messed with other email providers.  If you are using gmail to send an email, you will need to turn on allowing less secure apps at: https://myaccount.google.com/lesssecureapps .  I cannot verify if these are accurate or work, but they may be of some use to you:

For Gmail email adresses:
  SMTP Server = 'smtp.gmail.com'
  Port = 587

For Yahoo email addresses:
  SMTP Server = 'smtp.mail.yahoo.com'
  Port = 587

For Live or Hotmail email addresses:
  SMTP Server = 'smtp.live.com'
  Port = 587


Enjoy!
