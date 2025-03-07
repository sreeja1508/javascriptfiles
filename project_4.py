#CAESAR CIPER 
# 
alphbet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shiftkey):
    cipher_text=""
    for char in plain_text:
        if char in alphbet:
            position=alphbet.index(char)
            new_position=(position+shiftkey)%26
            cipher_text+=alphbet[new_position]
        else:
            cipher_text+=char    
    print(f"here's is the encryption result: {cipher_text}")    
def decryption(cipher_text,shiftkey):
    plain_text=""
    for char in cipher_text:
        if char in alphbet:
            position=alphbet.index(char)
            new_position=(position-shiftkey)%26
            plain_text+=alphbet[new_position]
        else:
            cipher_text+=char
    print(f"here's is the decryption result: {plain_text}") 
playagain=True
while playagain:
    a=input("type 'encrypt' for encryption ,type 'decrypt' for decryption\n")
    b=input("typer your message:\n").lower()
    c=int(input("enter the shift key:"))
    if a=='encrypt':
        encryption(plain_text=b,shiftkey=c)
    elif a=='decrypt':
        decryption(cipher_text=b,shiftkey=c)  
    wanna_end=input(" yes or no") 
    if wanna_end=='yes':
        playagain=False
        print("good byee") 

     
   