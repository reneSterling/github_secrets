import os

username=os.getenv("MY_USERNAME")
key=os.getenv("MY_API_KEY")

print("Hello," , username)
print("Your API key is" , key[:4] + "****")
