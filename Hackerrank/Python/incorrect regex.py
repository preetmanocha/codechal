import re
for i in range (int(input())):
    reg = input()
    try:
        re.compile(reg)
        print(True)
    except re.error:
       print(False)
