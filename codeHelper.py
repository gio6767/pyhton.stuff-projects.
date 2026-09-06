import itertools
import time

charset = "abcdefghijklmnopqrstuvwxyz"
target = "zzzzz"   # Change this to your own 5-letter test code

start = time.time()
attempts = 0

for attempt in itertools.product(charset, repeat=len(target)):
    guess = ''.join(attempt)
    attempts += 1

    if guess == target:
        elapsed = time.time() - start

        print("FOUND!")
        print("Code:", guess)
        print("Attempts:", attempts)
        print(f"Time: {elapsed:.4f} seconds")

        break