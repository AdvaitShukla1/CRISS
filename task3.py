text_file = open("input.txt", "r")
message=text_file.read()
text_file.close()
def findIndicator(message):
    for i in range(0,len(message)-4):
        if isUnique(message[i:i+5]):
            return i+1 #because indices start from 0 and we count from 1
def isUnique(str):
  for i in range(len(str)):
    for j in range(i + 1,len(str)):
      if(str[i] == str[j]):
        return False
  return True
print(f"The 1st indicator is present at position {findIndicator(message)}.")