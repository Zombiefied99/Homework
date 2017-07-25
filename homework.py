running = True
while running:
      num = input("How many sandwhiches can you eat? ")
      if num <= 0:
          print " You should try harder! Even a baby can eat 0 sandwhiches "
          running = False 
      else:
          brother = num + 1
          if num <= 4: 
              print 'My brother can eat ', brother, "sandwhiches." 
          else:
              print 'You will get sick if you eat that many sandwhiches!'
print 'You Lose!'       