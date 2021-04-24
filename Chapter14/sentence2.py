import re
import reprlib



RE_WORD=re.compile('\w+')
class Sentence:
    def __init__(self,text):
        self.text=text
        self.words=RE_WORD.findall(text)
    def __iter__(self):
        '''
        实现一个返回迭代器的__iter__方法
        即是 可迭代对象
        :return:
        '''
        return SentenceIterator(self.words)

    def __len__(self):
        return len(self.words)
    def __repr__(self):
        return "Sentence(%s)"%reprlib.repr(self.text)# 生成大型数据结构的简略字符串表示形式


class SentenceIterator:
    '''
    实现一个典型的迭代器
    '''
    def __init__(self,words):
        self.words=words
        self.index=0
    def __iter__(self):
        '''
        返回自身的__iter__
        :return:
        '''
        return self
    def __next__(self):
        '''
        返回下一个可用元素
        :return:
        '''
        try:
            word=self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index+=1
        return word



def test():
    sentence=Sentence("hello sentence ,welcome to the world")
    for word in sentence:
        print(word)

if __name__=='__main__':
    test()

