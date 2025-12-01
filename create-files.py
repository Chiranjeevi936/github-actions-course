from string import ascii_letters
import random

def generate_random_string() -> str:
    n = len(ascii_letters)
    random.randrange(0,n+1)
    random_string = ''.join( [ str(ascii_letters)[random.randrange(n)] for _ in range(100) ] )
    return random_string

files = ["file1.txt", "file2.json", "file3.yaml", "file4.txt", "tfile.txt", "gfile.txt"]

for file in files:
    with open(file, "w") as fp:
        fp.write(generate_random_string())




