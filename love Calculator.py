print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combined_name = name1+name2
lower_name = combined_name.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
first_word  = t + r + u + e
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_word  = l + o + v + e
score = int(str(first_word) + str(second_word))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40 ) and (score < 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


