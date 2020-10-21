import hashlib
import time

# Records the time of how long the program takes to achieve its goal.
start_time = time.time()

def hash(plain):
  # Hashlib's SHA1 require input to be encoeded in utf-8
  plain = plain.encode('utf-8')
  # Change the int at the end of this line to alter the number of nibbles being analysed by the program.
  first_hash = hashlib.sha1(plain).hexdigest()[:15]
  return first_hash

def floyd(hash, x0):
  tortoise = hash(x0)
  hare = hash(hash(x0))

  counter = 0
  final = ""
  print('first while')

  while (tortoise != hare):
    tortoise = hash(tortoise)
    hare = hash(hash(hare))
    counter += 1
    if (counter % 10000000 == 0):
      print(counter)
    
  tortoise = x0
  print('second while')
  counter = 0
   
  while (tortoise != hare):
    tortoise = hash(tortoise)
    hare = hash(hare)

    counter += 1
    if (counter % 10000000 == 0):
        print(counter)
    
    if (tortoise != hare):
        temp_tortoise = tortoise
        temp_hare = hare
        pass

    if (hash(tortoise) == hash(hare)):
        print('found hashes')
        print("tortoise:", temp_tortoise)
        print("hare", temp_hare)
        final = 'tortoise: ' + temp_tortoise + '\n' + 'hare: ' + temp_hare
        with open('hashes.log', 'w') as file_:
            file_.write(final)
        break

  print('Checking calculations...')
  print('tortoise', temp_tortoise, '>', hash(temp_tortoise))
  print('hare', temp_hare, '>', hash(temp_hare))

# Launching the main funciton
floyd(hash, 'extra')
# Printing the recorded time of completion
print("--- %s seconds ---" % (time.time() - start_time))