class Paperquantity:
  def __init__(self,q):
    self.q = q
    
  def getquantity(self):
    return (self.q*1.02+250)

class Paper:
    def __init__(self,x,y,gr):
        self.x = x
        self.y = y
        self.gr= gr

    def getweight(self):
        return (self.x*self.y*self.gr)

sheetprice = 0.9
forms = 1810
printstart = 1907
paperquantity = Paperquantity(1000)
totalpaper = (paperquantity.getquantity())
rashod_kraski = 1.46*totalpaper
#paper = Paper(100,0.7,0.02)
papercost = totalpaper*sheetprice
papercost = float("{0:.1f}".format(papercost))
print('papercost =',papercost)

class PrintCost():
  
  def getprintcost():
    return rashod_kraski+ forms + printstart
    print ('printcost=', PrintCost.getprincost)


def gettotalprintcost():
    return (PrintCost.getprintcost())+ papercost
    print (gettotalprintcost)

print ("paperquantity = ", paperquantity.getquantity())
print ("printcost = ", PrintCost.getprintcost())
print ("totalprintcost = " , gettotalprintcost())

class Sborka():
  def getsborka():
    return 1500 + 2*paperquantity.getquantity()+ 7.5*paperquantity.getquantity()+1*paperquantity.getquantity() + 3*paperquantity.getquantity()+13*paperquantity.getquantity()+1*paperquantity.getquantity()

'''
vyr = 1500 + 2*tv
    lam = tv*7.5 # 0.1 доллара США за кв.м. (для пакета 30х40) площадь = 1м
    podr = 2*tv
    tkl = tv*1
    ver = tv*3 
    skl = tv*13
    pik = tv*1
    sborka = vyr+lam+tkl+ver+skl+pik+podr
    print ('sborka=',sborka)
'''
print ("кол-во листов = ", paperquantity.getquantity())
print('sborka = ' ,Sborka.getsborka())

class Total():
  def gettotal():
    return Sborka.getsborka() + papercost + PrintCost.getprintcost()

print('total = ' ,Total.gettotal())