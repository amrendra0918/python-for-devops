text = "Python is awesome"
words = text.split()
print("Words:", words)

text2 = "This is great"
words = text2.split()
print("words:", words)

arn = "arn:aws:iam::123456789:user/jagjit"
print("The user is:", arn.split("/")[1])