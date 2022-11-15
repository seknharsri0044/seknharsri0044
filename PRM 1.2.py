#!/usr/bin/env python
# coding: utf-8

# In[22]:


'''A student will not be allowed to sit in the exam if his/her attendance is less than 75%. 
if he/she has medical causes reduce attendance criteria to 60%. Ask the user 
if he/she has a medical cause or not ( 'Y' or 'N' ) and print accordingly.
You were given a total no classes and total classes attended by the student.'''
N=int(input('enter total classes:'))
n=int(input('enter total  attended classes:'))
if ((n%N)*100)<75:
    print('true')
else:
    m=str(input('any  medical issue yes/No'))
    while( m=='Yes'):
        if((n%N)*100 >75)>60:
            print('True')
    else:
        print('False')

    

        
        


# In[23]:


class drawing:
    def triangle(self):
        
        print('your entered triangle sides')
        a=int(input('enter firts side a:'))
        b=int(input('enter second side b:'))
        c=int(input('enter third side c:'))
        if (((a+b)>c) or((a+c)>b) or ((b+c)>a)):
            print('valid triangle')
        else:
            print('invalid triangle')
    def rectangle(self):   
        print('your entered rectangle sides')
        a1=int(input('enter firts side a1:'))
        b1=int(input('enter second side b1:'))
        a2=int(input('enter third side a2:'))
        b2=int(input('enter fourth side b2:'))  
        if (a1==a2) or (b1==b2):
             print('valid rectangle')
        else:
            print('invalid rectangle')
s=drawing()
s.triangle()
s.rectangle()
            

        


# In[ ]:





# In[ ]:




