import hashlib
import binascii
import random
import string as string_module

counter = 0
comparison_list = {}

def get_random_string():
	letters = string_module.ascii_lowercase
	# This can produce bigger strings on which to perform the hashing.
	result_str = ''.join(random.choice(letters) for i in range(6))
	return result_str

while True:
	string = get_random_string()
	string = string.encode('utf-8')
	hash = hashlib.sha1(string)
	hex_dig = hash.hexdigest()
	# This integer will alter the amount of nibbles in the hash to be analysed
	var1 = hex_dig[:6]

	if var1 in comparison_list:
	    print('This took ',counter, ' calculations to arrive at. Here are the colliding strings:')
	    print('Sting 1 =', comparison_list[var1].decode('utf-8'))
	    print('String 2 =', string.decode('utf-8'))
	    break
	else:
	    comparison_list[var1] = string
	    counter += 1
