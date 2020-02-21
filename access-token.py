import os

token = raw_input("Enter your groupme access token: ") 

def write_to_file(token):
    f = open("bots/access-token.txt", "w+") 
    f.truncate(0)
    f.write(token) 
    f.close() 

write_to_file(token) 
