import time as t
str = "Hello World!"
alphabet = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ!"

print("\033[1;31m", end="")
for i in range(1, len(str) + 1):
    print("\r" + str[:i], end="")
    if i < len(str):
        for j in alphabet:
            t.sleep(0.05)
            print(j, end="")
            if j != str[i]:
                print("\b", end="")
            else:
                break
print("\033[0;0m")