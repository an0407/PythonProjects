#input email from user
email = input("Enter your email: ").strip()

#slice the username from email
username = email[:email.index('@'):]

#slice the domain name from the email
domain = email[email.index('@')+1:email.index('.'):]

#printing output
print(f"your username is {username}")
print(f"your domain is {domain}")