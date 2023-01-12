# format the file
def format_file():
    with open('D:\lic', "r") as f:
        lines = f.readlines()
    with open('D:\lic', "w") as f:
        for line in lines:
            str1 = line[0:9]
            if str1 == 'Users of ':
                f.write(line)
