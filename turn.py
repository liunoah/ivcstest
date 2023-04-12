# coding = utf-8
import os


def clearBlankLine():
    if os.path.exists("终秦结后.txt"):
        os.remove("终秦结后.txt")
    file1 = open('3.txt', 'r', encoding='utf-8') # 要去掉空行的文件
    file2 = open('终秦结后.txt', 'w', encoding='utf-8') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()

