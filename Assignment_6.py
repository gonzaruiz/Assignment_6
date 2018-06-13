
# coding: utf-8

# In[95]:


import math
def nthgeom(a,b,c):
    return a*(math.pow(b,(c-1)))

a = 2
b = 2
c = 2

nthgeom(a,b,c)


# In[112]:


#First I create the matrix using randon


# In[96]:


a = np.floor(10*np.random.random((3,3)))
print(a)



# In[ ]:


#Them I used Boolean argument


# In[97]:


b = a > 4
b


# In[ ]:


#Finally I make the 3 Geometric Progessions on the matrix using nthgeom


# In[105]:


first = nthgeom(9,2,5)


# In[106]:


first


# In[107]:


second = nthgeom(5,4,5) 


# In[108]:


second


# In[109]:


thrid = nthgeom(5,5,6)


# In[110]:


thrid

