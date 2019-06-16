Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> x = np.random.randint(10,100,20)
>>> y = x ** 2
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000002AE72859C50>]
>>> plt.show()
>>> plt.plot(x,y,'o')
[<matplotlib.lines.Line2D object at 0x000002AE732EC080>]
>>> plt.show()
>>> x = np.arange(1,100)
>>> y = x**2
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000002AE7333DDA0>]
>>> plt.show()
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x000002AE733A7128>
>>> plt.show()
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x000002AE75236278>
>>> plt.show()
>>> votes = [343,109,25,35]
>>> labels = ['BJP','CONG','SP+BSP','Others']
>>> plt.pit(x=votes,labels=labels)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    plt.pit(x=votes,labels=labels)
AttributeError: module 'matplotlib.pyplot' has no attribute 'pit'
>>> plt.pie(x=votes,labels=labels)
([<matplotlib.patches.Wedge object at 0x000002AE75265AC8>, <matplotlib.patches.Wedge object at 0x000002AE75270048>, <matplotlib.patches.Wedge object at 0x000002AE75270518>, <matplotlib.patches.Wedge object at 0x000002AE752709E8>], [Text(-0.5597131567974178, 0.946953632501544, 'BJP'), Text(0.18140443253896635, -1.0849389069690587, 'CONG'), Text(0.918349162485018, -0.6055037702302656, 'SP+BSP'), Text(1.0747309569235297, -0.2344213519077012, 'Others')])
>>> plt.show()
>>> plt.pie(x=votes,labels=labels,shadow=True,counterclock=False)
([<matplotlib.patches.Wedge object at 0x000002AE752A9EB8>, <matplotlib.patches.Wedge object at 0x000002AE752B2710>, <matplotlib.patches.Wedge object at 0x000002AE752B2E80>, <matplotlib.patches.Wedge object at 0x000002AE752BC630>], [Text(-0.5597131567974178, -0.946953632501544, 'BJP'), Text(0.18140443253896635, 1.0849389069690587, 'CONG'), Text(0.918349162485018, 0.6055037702302656, 'SP+BSP'), Text(1.0747309569235297, 0.2344213519077012, 'Others')])
>>> plt.show()
>>> plt.pie(x=votes,labels=labels,shadow=True,counterclock=True)
([<matplotlib.patches.Wedge object at 0x000002AE752EFE48>, <matplotlib.patches.Wedge object at 0x000002AE752F9668>, <matplotlib.patches.Wedge object at 0x000002AE752F9DD8>, <matplotlib.patches.Wedge object at 0x000002AE75304588>], [Text(-0.5597131567974178, 0.946953632501544, 'BJP'), Text(0.18140443253896635, -1.0849389069690587, 'CONG'), Text(0.918349162485018, -0.6055037702302656, 'SP+BSP'), Text(1.0747309569235297, -0.2344213519077012, 'Others')])
>>> plt.show()
>>> plt.pie(x=votes,labels=labels,shadow=True,counterclock=True,startangle=90)
([<matplotlib.patches.Wedge object at 0x000002AE75335F28>, <matplotlib.patches.Wedge object at 0x000002AE7533F748>, <matplotlib.patches.Wedge object at 0x000002AE7533FEB8>, <matplotlib.patches.Wedge object at 0x000002AE7534A668>], [Text(-0.9469536325015441, -0.5597131567974178, 'BJP'), Text(1.0849389069690587, 0.1814044325389663, 'CONG'), Text(0.6055037702302656, 0.918349162485018, 'SP+BSP'), Text(0.23442135190770125, 1.0747309569235297, 'Others')])
>>> plt.show()
>>> plt.pie(x=votes,labels=labels,shadow=True,counterclock=False,startangle=90,explode=[0,0,0.2,0])
([<matplotlib.patches.Wedge object at 0x000002AE752A9198>, <matplotlib.patches.Wedge object at 0x000002AE752A9908>, <matplotlib.patches.Wedge object at 0x000002AE752B2AC8>, <matplotlib.patches.Wedge object at 0x000002AE752B2EF0>], [Text(0.9469536325015441, -0.5597131567974177, 'BJP'), Text(-1.0849389069690587, 0.1814044325389669, 'CONG'), Text(-0.7155953648175865, 1.0853217374822939, 'SP+BSP'), Text(-0.23442135190770114, 1.0747309569235297, 'Others')])
>>> plt.show()
>>> plt.pie(x=votes,labels=labels,shadow=True,counterclock=False,startangle=90,explode=[0,0,0.5,0])
([<matplotlib.patches.Wedge object at 0x000002AE753906D8>, <matplotlib.patches.Wedge object at 0x000002AE75390400>, <matplotlib.patches.Wedge object at 0x000002AE752360F0>, <matplotlib.patches.Wedge object at 0x000002AE75236240>], [Text(0.9469536325015441, -0.5597131567974177, 'BJP'), Text(-1.0849389069690587, 0.1814044325389669, 'CONG'), Text(-0.8807327566985679, 1.335780599978208, 'SP+BSP'), Text(-0.23442135190770114, 1.0747309569235297, 'Others')])
>>> plt.show()
>>> plt.pie(x=votes,labels=labels,shadow=True,counterclock=False,startangle=90,explode=[0,0,0.5,0])
([<matplotlib.patches.Wedge object at 0x000002AE73308E48>, <matplotlib.patches.Wedge object at 0x000002AE732F6A58>, <matplotlib.patches.Wedge object at 0x000002AE732F6198>, <matplotlib.patches.Wedge object at 0x000002AE732FD0F0>], [Text(0.9469536325015441, -0.5597131567974177, 'BJP'), Text(-1.0849389069690587, 0.1814044325389669, 'CONG'), Text(-0.8807327566985679, 1.335780599978208, 'SP+BSP'), Text(-0.23442135190770114, 1.0747309569235297, 'Others')])
>>> plt.legend()
<matplotlib.legend.Legend object at 0x000002AE732FD978>
>>> plt.show()
>>> 
