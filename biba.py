#2018-04-10
#BY dazhige

bibas = []

class BIBA:
    def __init__(self,integrity,data,mode="trict"):
        self.integrity = integrity
        self.data = data
        #three modes: low,cycle,strict
        self.mode = mode
        bibas.append(self)
        #根据integrity属性排序
        bibas.sort(key=lambda x:x.integrity,reverse=False)
    def read(self,other):
        if self.mode=="cycle":
            pass
        elif self.mode=="low":
            if self.integrity>other.integrity:
                self.integrity = other.integrity
        else:
            assert self.integrity<=other.integrity
            #从高处往低处excute
            for i in range(0,bibas.index(other)-bibas.index(self)):
                bibas[bibas.index(other)-i].excute(bibas[bibas.index(other)-i-1])
        print(other.data)
    def write(self,other):
        assert self.integrity >= other.integrity
        other.data = self.data
        print("write over")
        #write
    def excute(self,other):
        assert self.integrity >= other.integrity
        print("{0} excute {1}".format(self.integrity,other.integrity))
        #excute