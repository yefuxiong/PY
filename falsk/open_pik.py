import pprint, pickle,json

list = open('list1.pik', 'rb')


class reg:
    def rega(self,phont,password,regFile):
        open_list =open(regFile,"rb")
        loadList = pickle.load(open_list)
        loadList =json.loads(loadList)
        for Listdata,valList in loadList.items():

            for listData in valList:
                #print(listData["title"],listData["rate"])
                pass
    '''
    写入用户信息，以【{}】形式
    '''
    def writUse(self,phont,password,writFile,writType):
        writOpen=open("list1.pik","rb")
        seeData=pickle.load(writOpen)
        pickle.load(writOpen)
        pickle(seeData)


txt = {"a":1,"b":1}
out =open(r"otu.pp","ab+")
pickle.dump(txt,out)
doc={"q:123"}
pickle.dump(doc,out)
out.close()
out=open(r"otu.pp","rb")
pickle.load(out)
print(pickle.load(out))
print(pickle.load(out))
print(pickle.load(out))
print(pickle.load(out))