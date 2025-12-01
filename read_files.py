from  pathlib import Path

files_list = sorted(Path('files').glob(pattern =  './file*'))

for  file in files_list:
    content = file.read_text()
    content_length = len(content)
    print(str(file.name).center(100,"-"))
    print(content)
    print()