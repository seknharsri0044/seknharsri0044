#!/usr/bin/env python
# coding: utf-8

# In[13]:


teams_performance={
   'GT':['GT',20,['W','W','L','L','W']]
    
   ,'LSG':['LSG',18,['W','L','L','W','W']]
    
   ,'RR':['RR',16,['W','L','W','L','L']]
    
    ,'DC':['DC',14,['W','W','L','W','L']]
    
    ,'RCB':['RCB',14,['L','W','W','L','L']]
    
    ,'KKR':['KKR',12,['L','W','W','L','W']]
    
    ,'PBKS':['PBKS',12,['L','W','L','W','L']]
    
    ,'SRH':['SRH',12,['W','L','L','L','L']]
    
    ,'CSK':['CSK',8,['L','L','W','L','W']]
    
    ,'MI':['MI',6,['L','W','L','W','W']]
   }


teams_performance


# In[2]:


teams_performance.keys()


# In[3]:


def retrive_team_two_losses(team): 
    for result in range(len(team[-1])-1):  
        if team[-1][result]==team[-1][result+1] and team[-1][result]=='L':    
            return team[0]
            


# In[14]:


# team having two consecutive losses
for team in teams_performance.keys():
    get_team=retrive_team_two_losses(teams_performance[team])
    if get_team is not None:
        print(get_team)

            


# In[8]:


def retrive_team_n_losses_or_wins(team,n):
    for i in range(len(team[-1])-n+1):
        if (team[-1][i:i+n]==['W']*n) or (team[-1][i:i+n]==['L']*n) :
            return team[0]  
        


# In[22]:


Y=True
while Y:
    n=int(input('enter the valid  value of consecutive losses or wins: '))
    if n>5:
        continue
    else:
        Y=False


# In[16]:


filtered_teams=[]
for team in teams_performance.keys():
    x=retrive_team_n_losses_or_wins(teams_performance[team],n)
    if x is not None:
        filtered_teams.append(x)
        print(x)    
print(filtered_teams)


# In[24]:


sum_of_points=0
for team in filtered_teams:
    sum_of_points+=teams_performance[team][1]
average_points=sum_of_points/len(filtered_teams)
print(average_points)
    


# In[ ]:




