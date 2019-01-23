from string import ascii_lowercase


# my idea
def decipher(text):

    decipherText = ""
    for c in text:
        if(c.isalpha()):
            c = chr(97 + ((ord(c)-ord('a') + 2) % 26))
        decipherText = decipherText + c

    print(decipherText)


# solution using string.maketrans()
def decipher2(text):

    intab = ascii_lowercase
    outtab = intab[2:] + intab[:2]
    trantab = str.maketrans(intab, outtab)

    print(str.translate(text, trantab))


cipherText = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagc" \
             "lr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

decipher(cipherText)
decipher2(cipherText)
