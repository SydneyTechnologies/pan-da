import random
import string
def generateHash():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase  
    numbers = "".join(str(i) for i in list(range(0, 10)))
    final_list = lowercase + uppercase + numbers
    hash = [ random.choice(final_list) for sel in range(7)]
    print("".join(hash))

