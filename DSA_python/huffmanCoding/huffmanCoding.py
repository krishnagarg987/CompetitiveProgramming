import heapq
import os
a='abbcccddddeeeeeffffffggggggg'

class binaryTreeNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None

    def __lt__(self, other):
        return self.value < other.value
    def __eq__(self, other):
        return self.value==other.value
    def __gt__(self, other):
        return self.value>other.value

class huffmancode:
    def __init__(self,path):
        self.path=path
        self.__minHeap=[]
        self.__hashedcodes={}
        self.__encodedText=""
        self.__bytesArray=[]
        self.__reversedcodes={}

    def __freqCount(self,string):
        dicti={}
        for i in string:
            dicti[i]=dicti.get(i,0)+1
        return dicti

    def __buildHeap(self,frequency):
        stringKeys=list(frequency.keys())
        for i in stringKeys:
            node=binaryTreeNode(i,frequency[i])
            heapq.heappush(self.__minHeap,node)

    def __binaryTree(self):
        while len(self.__minHeap)>1:
            element1=heapq.heappop(self.__minHeap)
            element2=heapq.heappop(self.__minHeap)
            sumofvalue=element1.value+element2.value
            node=binaryTreeNode(None,sumofvalue)
            node.left=element1
            node.right=element2
            heapq.heappush(self.__minHeap,node)
        return self.__minHeap[0]

    def __hashcodeshelper(self,treeNode,currBits):
        if treeNode is None:
            return
        if treeNode.key!=None:
            self.__hashedcodes[treeNode.key]=currBits
            self.__reversedcodes[currBits]=treeNode.key
            return
        self.__hashcodeshelper(treeNode.left,currBits+"0")
        self.__hashcodeshelper(treeNode.right,currBits+"1")

    def __hashcodes(self,treeNode):
        self.__hashcodeshelper(treeNode,"")

    def __codedText(self,string):
        for i in string:
            self.__encodedText+=self.__hashedcodes[i]

    def __paddedString(self):
        add=8-len(self.__encodedText)%8
        self.__encodedText+="0"*add
        padded_info="{0:08b}".format(add)
        self.__encodedText=padded_info+self.__encodedText

    def __bytesString(self):
        for i in range(0,len(self.__encodedText),8):
            byte=self.__encodedText[i:i+8]
            self.__bytesArray.append(int(byte,2))

    def compress(self):
        file_path,extension=os.path.splitext(self.path)
        output_path=file_path+'.bin'
        with open(self.path,'r+') as file , open(output_path,'wb') as output:
            text=file.read()
            text=text.strip()
            frequencyCount=self.__freqCount(text)
            self.__buildHeap(frequencyCount)
            treeNode=self.__binaryTree()
            self.__hashcodes(treeNode)
            self.__codedText(text)
            self.__paddedString()
            self.__bytesString()
            final_bytes=bytes(self.__bytesArray)
            output.write(final_bytes)
        print("compressed")
        return output_path

    def findActualText(self,bit_string):
        paddedcount=bit_string[:8]
        intpaddedcount=int(paddedcount,2)
        text=bit_string[8:]
        text=text[:-1*intpaddedcount]
        return text

    def bitToText(self,actual_text):
        decodedText=""
        currbits=""
        for bit in actual_text:
            currbits+=bit
            if self.__reversedcodes.get(currbits,False):
                decodedText+=self.__reversedcodes[currbits]
                currbits=""
        return decodedText

    def decompress(self,input_path):
        file_name,extension=os.path.splitext(input_path)
        decompressed_output=file_name+'_decompressed'+'.txt'
        with open(input_path,'rb') as file,open(decompressed_output,'w') as output:
            bit_string=""
            byte=file.read(1)
            while byte:
                encodedByte=ord(byte)
                encodeedBit=bin(encodedByte)[2:].rjust(8,'0')
                bit_string+=encodeedBit
                byte=file.read(1)
            actual_text=self.findActualText(bit_string)
            finaldata=self.bitToText(actual_text)
            output.write(finaldata)

path='/home/krxxnna/Downloads/sample.txt'
h=huffmancode(path)
output_path=h.compress()
h.decompress(output_path)

