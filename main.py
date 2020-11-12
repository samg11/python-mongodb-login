# PASTE YOUR CONNECTION STRING HERE
connection_string=""

# pip install pymongo
import pymongo
from pymongo import MongoClient

cluster = MongoClient(connection_string)
db = cluster["test"]
collection = db["test"]

def add_user(username,password):
    if int(collection.count_documents({ "username" : username })) == 0:
        post = {
            "_id":int(collection.count_documents({})),
            "username":username,
            "password":password
            }
        collection.insert_one(post)

        if int(collection.count_documents({ "username" : username })) == 1:
            print('account creation successful')

    else:
        print('That username has been taken please try again')
        add_user()

def login(username,password):
    if int(collection.count_documents({ "username" : username })):
        if int(collection.count_documents({ "username":username, "password":password })):
            print("Authentication Successful!")

        else:
            print("Password is incorrect")

    else:
        print('That Username is invalid')

def main():
    add_or_create = input("Would you like to create an accout or login? ")

    if add_or_create.lower() == "create":
        add_user(
            input("Username: "),
            input("Password: ")
            )

    if add_or_create.lower() == "login":
        login(
            input("Username: "),
            input("Password: ")
            )

if __name__ == "__main__":
    print("Look at the README.md before running this code")
    main()
