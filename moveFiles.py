import os
import shutil

default = "C:\\Users\\LYMJa\\Desktop\\"
word = "C:\\Users\\LYMJa\\Desktop\\word"
excel = "C:\\Users\\LYMJa\\Desktop\\excel"
prod = "C:\\Users\\LYMJa\\Desktop\\产品密钥"
xmind = "C:\\Users\\LYMJa\\Desktop\\xmind"
txt = "C:\\Users\\LYMJa\\Desktop\\txt"

def Move(path):
    ls = os.listdir(path)
    if len(ls) != 0:
        for fi in ls:
            s = os.path.splitext(fi)
            p = default + fi
            if ".doc" in s[1]:
                shutil.move(p, word)
            elif ".xls" in s[1]:
                shutil.move(p, excel)
            elif s[1] == ".xmind":
                shutil.move(p, xmind)
            elif s[1] == ".jks":
                shutil.move(p, prod)
            elif s[1] == ".txt":
                shutil.move(p, txt)

if __name__ == '__main__':
    Move(default)
