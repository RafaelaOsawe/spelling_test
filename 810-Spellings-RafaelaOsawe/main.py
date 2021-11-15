data = open("spellings.csv", "a")
print("Hello")

spelling_test = []
spelling_tally = 0

print("Welcome to your weekly spelling test!")
print()
print("Please enter your name: ")
name = input().lower()
data.write(name)
print()
print("Please spell out the word 1: ")
word1 = input().lower()

if word1 == "adorable":
  print("Well done! 1 point earned.")
  spelling_tally = spelling_tally + 1
  data.write("Correct") 
else:
  print("That is incorrect. ")
  data.write("Incorrect")
print()
print("Please spell out the word 2: ")
word2 = input().lower()

if word2 == "applicable":
  print("Well done! 1 point earned.")
  spelling_tally = spelling_tally + 1
  data.write("Correct")
else:
  print("That is incorrect. ")
  data.write("Incorrect")
print()
print("Please spell out the word 3: ")
word3 = input().lower()

if word3 == "considerable":
  print("Well done! 1 point earned.")
  spelling_tally = spelling_tally + 1
  data.write("Correct")
else:
  print("That is incorrect. ")
  data.write("Incorrect")
print()
print("Please spell out the word 4: ")
word4 = input().lower()

if word4 == "tolerable":
  print("Well done! 1 point earned.")
  spelling_tally = spelling_tally + 1
  data.write("Correct")
else:
  print("That is incorrect. ")
  data.write("Incorrect")
print()
print("Please spell out the word 5: ")
word5 = input().lower()

if word5 == "desirable":
  print("Well done! 1 point earned.")
  spelling_tally = spelling_tally + 1
  data.write("Correct")
else:
  print("That is incorrect. ")
  data.write("Incorrect")
print()
print("Please spell out the word 6: ")
word6 = input().lower()

if word6 == "believable":
  print("Well done! 1 point earned.")
  spelling_tally = spelling_tally + 1
  data.write("Correct")
else:
  print("That is incorrect. ")
  data.write("Incorrect")
print()
print("Please spell out the word 7: ")
word7 = input().lower()

if word7 == "excitable":
  print("Well done! 1 point earned.")
  spelling_tally = spelling_tally + 1
  data.write("Correct")
else:
  print("That is incorrect. ")
  data.write("Incorrect")
print()
print("Please spell out the word 8: ")
word8 = input().lower()

if word8 == "regrettable":
  print("Well done! 1 point earned.")
  spelling_tally = spelling_tally + 1
  data.write("Correct")
else:
  print("That is incorrect. ")
  data.write("Incorrect")
print()
print("You scored a total of ",spelling_tally, " out of 8.")

data.close()
