#Random number 

import random
print(random.random())

f= open("randomnumbers.txt", "w")
f.write(str(random.random()))
f.close()

