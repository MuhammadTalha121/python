import random
import string

# we are creating a random password gerator:

# code it//

length = 10
# Generation with random..\ string.. module ::
password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
print("Your Password Is ready: Length is ", length, ":", password)