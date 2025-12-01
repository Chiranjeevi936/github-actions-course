files = ["file1.txt", "file2.json", "file3.yaml", "file4.jpeg"]

for file in files:
    with open(file, "w") as fp:
        fp.write(file)