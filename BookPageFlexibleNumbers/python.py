
lowPage=1
highPage=1000
midPage=0
numLoops=0
target = int(input("G'day. I'm a book with 1000 pages. What page do you want to see?"))
while ((((highPage - lowPage) > 2)) and (target != midPage)):
  numLoops = numLoops + 1
  print("Now looking for your page, between page", lowPage, "and page", highPage)
  midPage = int((lowPage + highPage) /2)
  if midPage < target:
    lowPage = midPage + 1
  elif midPage > target:
    highPage = midPage - 1
  else:
      print("Here's your page!")

print ("We finished between page",  lowPage, "and page", highPage)
print ("We found the right page after", numLoops, "attempts.")
