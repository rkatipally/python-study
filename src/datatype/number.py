import sys
from decimal import Decimal as D
def showNumbers():
    print(2/5)
    print(2//5)
    print(-7/4)
    print(-7//4) #Floor
    print(int(-7/4)) #Truncate to an integer
    print('Reminder:: ' + str(10%3))

    print('=========Real===========')
    print(sys.float_info)

    print('=========Decimal===========')
    print(D(3.14))
    print(D('3.14'))
    print(D(0.1)*D(3) - D(0.3))
    print(D('0.1')*D('3') - D('0.3'))

showNumbers()