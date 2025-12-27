import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak("WElCOME TO OUR RESTAURANT CAN YOU CHOOSE THE MENU LISTED BELOW")
choice=int(input("Select the options: 1.idli, 2.dosa, 3.pongal, 4.exist"))
if (choice==1):
    print("idli")
elif (choice==2):
    print("dosa")
elif(choice==3):
    print("pongal")
else:
    print("exit")
    speak("Thank you for visiting. Goodbye")

if choice in [1, 2, 3]:
  speak("YOUR ORDER WILL BE DELIVERED WITHIN 5 MINUTES")

payment_choice=int(input("Enter payment choice: 1.cash, 2.UPI,"))
if (payment_choice==1):
    print("cash")
elif (payment_choice==2):
    print("UPI")
    speak("QR will be visible now")
else:
    print("invalid choice")
if payment_choice==1:
    speak("Thank you for visiting. Goodbye")
else:
    speak("payment is successfull")




