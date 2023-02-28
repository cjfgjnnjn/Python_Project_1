print("=======Welcome to Tillu Academy=======")
_name_ = input("Enter your name here:")
e_mail = input("Enter your E-mail ID here:")
e1 = input("WE have just send you an OTP on your given E_mail ID.\n WAit for sometime and Enter here the OTP to verify:")
import random
randNumber = random.randint(1451, 12721)
email_body = random.randint(1451, 12721)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def mail_fication():
    password = "cswv kuxx vsos mldx"
    me = "singhavijit395@gmail.com"
    #you = e_mail

    email_body = random.randint(1451, 12721)
    you = e_mail


    message = MIMEMultipart('alternative', None, [MIMEText(email_body, 'html')])

    message['Subject'] = ''
    message['From'] = me
    message['To'] = you

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(me, password)
        server.sendmail(me, you, message.as_string())
        server.quit()
        print(f'Email sent: {email_body}')
    except Exception as e:
        print(f'Error in sending email: {e}')
import time
t = time.strftime('%H:%M:%S')
h = int(time.strftime("%H"))
if(h>=0 & h<12):
    print("Good morning Mr." + _name_)
elif(h>=12 and h<17):
  print("Good Afternoon Sir!" + _name_)
elif(h>=17 and h<0):
  print("Good Night Sir!" + _name_)
a = int(input(_name_ + ", enter your age here:"))
# Avijit_Singh = 51843065163
# Jitesh_Singh = 76387879387



b = 18
c = 80
a1 = "1.New license" or "a1"
a2 = "2.License Update" or "a2"
a3 = "3.Correction in my License" or "a3"

def Babu_ghat():
   if e1==email_body:
       avijit_singh()
   else:
       print("Sorry your OTP is invalid")



def genda_swami():
    print("Please enter the required details:")
    h1 = input("Name:")
    h2 = input("Father's name:")
    h3 = input("Your phone number:")
    print(
        h1 + "\n" + h2 + "\n" + h3 + "\n" + "Your apointment has been booked. Date and Time will be informed you on the number provided by you")
    print("YOUR PASSWORD FOR APPOINTMENT IS :")
    print(random.randint(1451, 12721))


def dhuk_dhuk_paro():
    b1 = input("Enter your name here(block):")
    b2 = input("Enter you father's name here:")
    b3 = input("Enter your residential address here:")
    b4 = input("Enter you phone number here:")
    print((b1 + "\n" + b2 + "\n" + b3 + "\n" + b4 + "\n" + "What do you want to change"))
    A = "Name"
    print(A)
    B = "Fathers name"
    print(B)
    C = "Address"
    print(C)
    D = "phone number"
    print(D)
    gh1 = input("Enter the data here you wants to change(Only one can be changed. For more contact on 982344265):")
    if gh1 == A or B or C or D:
        print("Done! Apply for new license here only")


def avijit_singh():
    if a >= b:
        Dom_Gopal()
    elif(a < b or a>80):
        print("you are not eligible for this program")
    elif a > c:
        print("Invalid input")
        avijit_singh()
    else:
        avijit_singh()


def Dom_Gopal():
    print("Please follow us further with this options,")
    print(a1, "\n", a2, "\n", a3)
    # w1 = input("Enter your required service here:")
    kali_champa()


def kali_champa():
    w1 = input("Enter your required service here:")
    if w1 == a1:
        barmunda()
    elif w1 == a2:
        genda_swami()
    elif w1 == a3:
        dhuk_dhuk_paro()
    else:
        avijit_singh()


def barmunda():
    b1 = input("Enter your name here(block):")
    b2 = input("Enter you father's name here:")
    b3 = input("Enter your residential address here:")
    b4 = input("Enter you phone number here:")
    print("Your name is: " + b1)
    print("You father's name is: " + b2)
    print("Your residebtial address is: " + b3)
    print("Your phone number is: " + b4)
    print("Your apointment has been booked.\n YOUR PASSWORD FOR APPOINTMENT IS:")
    print(random.randint(1451, 12721))
mail_fication()
Babu_ghat()
