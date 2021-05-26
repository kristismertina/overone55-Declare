import datetime
class Declare:
    def __init__ (self, heading, descip, aurhor):
        self.__heading = heading
        self.__descip = descip
        self.__aurhor = aurhor
        self.__datetime = datetime.datetime.today()
        self.__looking = 0

    def __str__ (self):
        return f"{self.__heading}, {self.__descip}, {self.__aurhor}, {self.__datetime} , {self.__looking}"

    def looking (self):
        self.__looking +=1
        print(self)


    def change_heading (self, name):
        self.__heading = name
        return self.__heading

    def change_descip (self, name):
        self.__descip = name
        return self.__descip



a = Declare("Animals", "cat dog fish elefant", "Paul Down")
#print(a.change_descip("dffddf"))
#print(a.change_heading("hjhhhhjnnnnn"))
print (a.looking())
