class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
from itertools import cycle
#p = ['id','+','id','*','id',' ']
#p = ['id','*','id','-','id','*','id',' ']
#p = ['id','+','id','*','id','*','id','-','id','+','id',' ']
#p = ['id','/','id','-','id','+','id','*','id','-','id','+','id',' ']
#p = ['id','-','(','id','+','id',')',' ']
#p = ['id','*','(','id','*','id','+','id',')','*','id',' ']
a = []
b =[]
c = []
d = []
gata = False
plus = False
minus = False
ori = False
imparte = False
identificator = True
parDesch = False
parInch = False
sir = ['E']

v = 0
def E():
    print 'am intrat in E()'
    global sir, a, b, c, d, v
    global plus
    global minus
    global ori
    global imparte
    global identificator
    global parDesch
    global parInch
    for i in range(len(sir)):
        if sir[i] == 'E':
            sir.pop(i)
            sir.insert(i, 'E1')
            sir.insert(i, 'T')
            print sir
            T()
            Eprim()
def T():
    global sir,a,b,c,d,v
    global plus
    global minus
    global ori
    global imparte
    global identificator
    global parDesch
    global parInch
    for i in range(len(sir)):
        if sir[i] == 'T':
            if i != 0:
                sir.insert(i,'T1')
                sir.insert(i,'F')
                sir.remove('T')
                print sir
                F()
                Tprim()
            else:
                sir.remove('T')
                sir.insert(0,'T1')
                sir.insert(0,'F')
                print sir
                F()
                Tprim()

def F():
    global sir,a,b,c,d,v
    global identificator
    global parDesch
    global parInch
    if identificator == False and parDesch == False:
        VeziUrm()
    for i in range(len(sir)):
        if sir[i] == 'F':
            if identificator == True:

            #sir.remove('F')

                sir.insert(i,'id')
                sir.remove('F')
                print sir
                identificator = False
            #VeziUrm(p)
            if parDesch == True:
                sir.insert(i,')')
                sir.insert(i,'E')
                sir.insert(i,'(')
                parDesch = False
                sir.remove('F')
                E()


def Eprim():
    global sir,a,b,c,d,v,s1,gata
    global ori
    global imparte
    global plus
    global minus
    global identificator
    global parDesch
    global parInch
    if gata == False:
        if identificator == False and parDesch == False:
            VeziUrm()
    if plus == True and parInch == False:
        for i in range(len(sir)):
            if sir[i] == 'E1':
                sir.insert(i,'T')
                sir.insert(i,'+')
                plus = False
                print sir
                T()
                Eprim()
    elif minus == True and parInch == False:
        for i in range(len(sir)):
            if sir[i] == 'E1':
                sir.insert(i,'T')
                sir.insert(i,'-')
                minus = False
                print sir
                T()
                Eprim()
    #if identificator == True and parInch == False:
        #if sir.__contains__('E1'):
            #sir.remove('E1')
            #print sir
    elif parInch == True:
        for i in range(len(sir)):
            if sir[i] == 'E1':
                sir.pop(i)
                parInch = False
                break
    #print identificator, parInch, parDesch, plus, minus, ori, imparte
    elif identificator == False and parInch == False and parDesch == False and plus == False and minus == False and ori == False and imparte == False:
        if sir.__contains__('E1'):
            sir.remove('E1')
            print sir

def VeziUrm():
    global s1
    if s1.size() != 0:
        CeUrmeaza(s1.pop())



def Tprim():

    global sir,s1
    global gata
    global plus
    global minus
    global ori
    global imparte
    global identificator
    global parDesch
    global parInch
    if gata == False:
        if identificator == False and parDesch == False:
            VeziUrm()
    if ori == True:
        for i in range(len(sir)):
            if sir[i] == 'T1':
                sir.insert(i,'F')
                sir.insert(i,'*')
                ori = False
                print sir
                F()
                Tprim()
    elif imparte == True:
        for i in range(len(sir)):
            if sir[i] == 'T1':
                sir.insert(i,'F')
                sir.insert(i,'/')
                imparte = False
                print sir
                F()
                Tprim()
    else:
        sir.remove('T1')
        print sir


def CeUrmeaza(x):
    global plus
    global minus
    global ori
    global imparte
    global identificator
    global parDesch
    global parInch
    global gata

    if x == '+':
        plus = True
        #print '+'
    elif x == '-':
        minus = True
        #print '-'
    elif x == '*':
        ori = True
        #print '*'
    elif x == '/':
        imparte = True
        #print '/'
    elif x == 'id':
        identificator = True
        #print 'id'
    elif x == '(':
        parDesch = True
        #print '('
    elif x == ')':
        parInch = True
    elif x == ' ':
        gata = True
        #print 'spatiu'

def Genereaza(token):
    global sir,v
    global identificator, plus, minus, ori, imparte
    global parDesch
    global parInch
    VeziUrm()
    if token == '+':
        for i in range(len(sir)):
            if sir[i] == 'E1':
                sir.insert(i,'T')
                sir.insert(i,'+')
                plus = False
                print sir
                T()
                Eprim()
    if token == '-':
        for i in range(len(sir)):
            if sir[i] == 'E1':
                sir.insert(i, 'T')
                sir.insert(i, '-')
                minus = False
                print sir
                T()
                Eprim()
    if token == '*':
        for i in range(len(sir)):
            if sir[i] == 'T1':
                sir.insert(i,'F')
                sir.insert(i,'*')
                ori = True
                print sir
                F()
                Tprim()
    if token == '/':
        for i in range(len(sir)):
            if sir[i] == 'T1':
                sir.insert(i, 'F')
                sir.insert(i, '/')
                imparte = True
                print sir
                F()
                Tprim()
    if token == 'id':
        for i in range(len(sir)):
            if sir[i] == 'E':
                if i != 0:
                    sir.insert(i,'E1')
                    sir.insert(i,'T')
                    c.remove('E')
                    identificator = True
                    print sir
                    T()
                    Eprim()
                else:
                    sir.insert(0,'E1')
                    sir.insert(0,'T')
                    print sir
                    sir.remove('E')
                    T()
                    Eprim()


def Parcurge(p1):
    global sir,p,s1
    p1 = p[:]
    print 'sirul este', p
    element = s1.pop()
    print len(p)
    print sir
    Genereaza(element)

s1 = Stack()
for i in reversed(range(len(p))):
    s1.push(p[i])
print Parcurge(p)


