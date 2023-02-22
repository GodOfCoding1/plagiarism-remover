hashMap={
    "a": [
        "\u0430",
        "\u00e0",
        "\u00e1",
        "\u1ea1",
        "\u0105"
    ],
    "c": [
        "\u0441",
        "\u0188",
        "\u010b"
    ],
    "d": [
        "\u0501",
        "\u0257"
    ],
    "i": [
        "\u0456",
        "\u00ed",
        "\u00ec",
        "\u00ef"
    ],
    "j": [
        "\u0458",
        "\u029d"
    ],
    "n": [
        "\u0578"
    ],
    "o": [
        "\u043e",
        "\u03bf",
        "\u0585",
        "\u022f",
        "\u1ecd",
        "\u1ecf",
        "\u01a1",
        "\u00f6",
        "\u00f3",
        "\u00f2"
    ],
    "p": [
        "\u0440"
    ],
    "q": [
        "\u0566"
    ],
    "u": [
       
        "\u057d",
       
    ],
    "x": [
        "\u0445",
        "\u04b3"
    ],
    "y": [
        "\u0443",
        "\u00fd"
    ]
}

import docx

def getTextFromDoc(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def replaceSpace(s:str):
    specialStr="​"
    newS=s.replace(" ",specialStr)
    weridChar="𝅴𝅹"
    print(specialStr in newS)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(newS)

def replaceLetters(s:str):
    
    newS=""
    counter=0
    allowConsecutive=3
    gap=13
    s=s.split(" ")
    for word in s:
        if counter%gap==0 or allowConsecutive>0:
            res=""
            for i in word:
                if i in hashMap:
                    res+=hashMap[i][0]
                else:
                    res+=i
            newS+=res+" "
            allowConsecutive=allowConsecutive-1 if counter%gap!=0 else 4
        else:
            newS+=word+" "
        counter+=1
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(newS)

# use below lines for using input texts
# with open("input.txt","r") as input:
#     replaceLetters(input.read())

replaceLetters(getTextFromDoc("sample.docx"))