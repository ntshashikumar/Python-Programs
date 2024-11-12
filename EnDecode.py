import base64

def encoder():
    Message=input("Enter message to encoded : ")
    msg_bytes=bytes(Message,'utf-8')
    en_msg=base64.b64encode(msg_bytes)
    print(f"Encoded Message :{en_msg}")

def decoder():
    msg2=input("Enter message to decode :")
    msg2_bytes=bytes(msg2,"utf-8")
    de_msg=base64.b64decode(msg2_bytes)
    print(f"Decoded Message : {de_msg}")

print("Python Encoder and Decoder")
while 1:
    print("\n1.Encoder \n2.Decoder \n3.Exit")
    option=int(input("Select any one option :"))

    if option==1:
        encoder()
    elif option==2:
        decoder()
    elif option==3:
        exit()
    else:
        print("wrong Choice! Try Again")

'''
msg2="U2hhc2hp" # Shashi
msg2="U2hhc2hpa3VtYXI=" # Shashikumar
'''