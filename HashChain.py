import hashlib

some_string = "ecsc"

numberOfEncrypts = 0

currentHash = some_string
success = False
while success == False:
    if currentHash == "c89aa2ffb9edcc6604005196b5f0e0e4":
        print("---------------------------------")
        print("Success, number of encryptions = " + str(numberOfEncrypts) )
        success = True
    else:
        hash = None
        hash = hashlib.md5()
        hash.update(currentHash)
        currentHash = hash.hexdigest()
        numberOfEncrypts = numberOfEncrypts + 1
        print("hash line : " + str(numberOfEncrypts) + " " + str(currentHash))



