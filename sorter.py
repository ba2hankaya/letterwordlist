filename = input("filename: ")
wordlen = int(input("wordlength: "))
fileout = input("fileout: ")
f2 = open(fileout,"w+")
with open(filename, 'r') as f:
    try:
        for word in f:
            word = str(word).strip()
            if(len(word) == wordlen):
                f2.write(str(word) + "\n")
    except:
        print("error")

print("done")
f2.close()
                
