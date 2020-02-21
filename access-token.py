import os

token = input("Enter your groupme access token: ") 

def write_to_file(token):
    f = open("bots/access-token.txt", "w+") 
    f.truncate(0)
    f.write(token) 
    f.close() 
    print('Wrote access token to file!')

write_to_file(token) 
