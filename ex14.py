from sys import argv

script, user_name, password = argv
prompt = 'enter: '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print("Do you like me?")
likes = input(prompt)

print(f"Where you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so your password is {password}. You said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
