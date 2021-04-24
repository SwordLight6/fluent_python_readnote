import re
import reprlib

'''
实现一个简易的序列类
'''

RE_WORD=re.compile('\w+')
class Sentence:
    def __init__(self,text):
        self.text=text
        self.words=RE_WORD.findall(text)
    def __getitem__(self, index):
        return self.words[index]
    def __len__(self):
        return len(self.words)
    def __repr__(self):
        return "Sentence(%s)"%reprlib.repr(self.text)# 生成大型数据结构的简略字符串表示形式


def test():
    sentence=Sentence("hello sentence ,welcome to the world")
    for word in sentence:
        print(word)

if __name__=='__main__':
    test()

