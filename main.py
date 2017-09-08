# Python 3
def check(a):
  try:
    int(a)
  except:
    return False

userinput = ""

while check(userinput) == False:
  userinput = input("Enter a number")
