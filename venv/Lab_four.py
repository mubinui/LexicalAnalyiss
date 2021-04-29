import re

methods = []
retrn_typ = []
method_pattern = "^(public)\s(static)?(\s)?(void|int|double|String|boolean)\s(\w)+(\s)?\(([\s]?(int|double|String|boolean)\s(\w)+[,]?)*\)$"
f = open("input.txt", "r")
x = f.readlines()
text = str(x)
testy = text.split("\n")
for i in range(len(x)-1):
    stra = x[i]
    m_tester = re.compile(method_pattern)
    xy = m_tester.search(stra)

    if xy!=None:
        a = str(xy.group())
        if not a.__contains__("void"):
            if a.__contains__("static"):

                if a.__contains__("int"):
                    methods.append(a[18:])
                    retrn_typ.append("int")

            else:
                if a.__contains__("int"):
                    methods.append(a[11:])
                    retrn_typ.append("int")

        else:
            if a.__contains__("static"):
                methods.append(a[18:])
                retrn_typ.append("void")
            else:
                methods.append(a[12:])
                retrn_typ.append("void")



print("Methods->")

for p in range(len(methods)):
    print(methods[p],", return type:",retrn_typ[p])
