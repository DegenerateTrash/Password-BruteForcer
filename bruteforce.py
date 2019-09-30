def getpassword():
    password = str(input("Password: "))
    return password
def brutepass(password):
    import time
    start = time.time()
    i = 32
    passw = []
    let = 0
    for letter in password:
            passw.append("")
    while i >= 32  and i <= 127 and let != len(password):
        passw[let] = str(chr(i))
        if passw[let] == password[let]:
            let += 1
        i += 1
        if i > 127:
            i = 32
        #print(chr(i))
    print("".join(passw))
    print("Took {0:0.50f} seconds to guess {1}".format(time.time() - start,password))
    return password

def main():
    password = getpassword()
    brutepass(password)
    return
main()