# Write a password generator in Python.
# Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords should be
# random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

import string
import random


def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))

