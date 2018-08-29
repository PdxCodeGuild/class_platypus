def title_file(path):
    with open(path, 'r') as f:
        return f.read()

print(title_file('title.txt'))