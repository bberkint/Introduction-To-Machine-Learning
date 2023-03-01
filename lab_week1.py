#!/usr/bin/env python
# coding: utf-8

# In[ ]:


var1 = 29
var2 = 34

day = "sunday"

var3 = 10.0


# In[1]:


list_int = [1,2,3,4,5]
type(list_int)


# In[2]:


value = list_int[3]
print(value)


# In[4]:


value


# In[5]:


list_int[-1]


# In[6]:


list_int[0:3]


# In[8]:


dir(list_int)


# In[14]:


list_int.append(7)
print(list_int)


# In[19]:


list_int.remove(7)
print(list_int)


# In[20]:


list_int.reverse()
print(list_int)


# In[22]:


list_int.sort()
print(list_int)


# In[23]:


for each in range(1,11):
    print(each)


# In[26]:


liste = [1,2,3,4,6,8,9,7,1]
sum(liste)
min(liste)


# In[28]:


minimum = 10000
for each in liste:
    if(each<minimum):
        minimum = each
    else:
        continue
print(minimum)        


# In[30]:


i = 0

while (i < 4):
    print(i)
    i= i+1


# In[32]:


def cember_cevre(r,pi=3.14):
    
    
    """
    Çember Çevresi 
    
    """
    output = 2*pi*r
    
    return output

cember_cevre(2)


# In[35]:


def hesapla(x):
    output = x*x
    return output

hesapla(5)

sonuc = lambda x: x*x
print(sonuc(4))


# In[37]:


dictionary = {"Berkin":23, "Mustafa": 25,"Serkan":38}

dictionary["Berkin"]


# In[38]:


dictionary.keys()


# In[41]:


dictionary.values()


# In[43]:


def deneme():
    dictionary = {"Berkin":23, "Mustafa": 25,"Serkan":38}
    
    return dictionary

dic = deneme()
print(dic)


# In[46]:


keys = dictionary.keys()

if "Berkin" in keys:
    print("evet")
else:
    print("hayır")

