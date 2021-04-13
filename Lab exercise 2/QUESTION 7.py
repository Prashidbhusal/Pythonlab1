#Game finding a secret number with in three attempt using while loop.
secret_number=9
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess=int(input('guess : '))
    guess_count += 1
    if guess == secret_number:
        print('YOU WON!')
        break
else:
    print('SORRY ,YOU FAILED!!')



