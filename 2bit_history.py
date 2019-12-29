# coding=UTF-8
import numpy as np
REG0=0
REG1=0
REG2=0
REG3=0
def REGstate():#Display 2BC state
    global REG0,REG1,REG2,REG3
    str1=str(REG0)
    str2=str(REG1)
    str3=str(REG2)
    str4=str(REG3)
    strsum=str1+','+str2+','+str3+','+str4
    trans=strsum.replace('0','SN').replace('1','WN').replace('2','WT').replace('3','ST')#00=SN,01=WN,10=WT,11=ST
    print('2BC State:'+trans)
def changeREG(x,y):#accoding history to change REG value
    global REG0,REG1,REG2,REG3
    if x=='00':
        if y=="T":
            if REG0==3:#if REG's value=3 and outcome=T,REG=ST,so value is not change
                REG0=3
            else:
                REG0=REG0+1
        else:
            if REG0==0:#if REG's value=0 and outcome=N,REG=SN,so value is not change
                REG0=0
            else:
                REG0=REG0-1
    elif x=='01':
        if y=="T":
            if REG1==3:
                REG1=3
            else:
                REG1=REG1+1
        else:
            if REG1==0:
                REG1=0
            else:
                REG1=REG1-1
    elif x=='10':
        if y=="T":
            if REG2==3:
                REG2=3
            else:
                REG2=REG2+1
        else:
            if REG2==0:
                REG2=0
            else:
                REG2=REG2-1
    elif x=='11':
        if y=="T":
            if REG3==3:
                REG3=3
            else:
                REG3=REG2+1
        else:
            if REG3==0:
                REG3=0
            else:
                REG3=REG3-1

def history(x):#history is represent need to chose which REG
    if x=='NN':
        x='00'
    elif x=='NT':
        x='01'
    elif x=='TN':
        x='10'
    elif x=='TT':
        x='11'
    return x
def select(x):#According history to chose REG to prediction
    if x=='00':
        pred=REG0
    elif x=='01':
        pred=REG1
    elif x=='10':
        pred=REG2
    elif x=='11':
        pred=REG3
    return pred
def prediction(x): #According choose REG's value to predicted
    if x<=1:
        return 'N'
    else:
        return 'T'
if __name__ == "__main__":
    f = open('./input.txt', 'r')
    line = f.readline()
    str1=line.strip('\n')

    outcome=str1.split(',')
    initialstate0='N'##Initial state
    initialstate1='N'#Initial state
    missrate=0
    for i in range (len(outcome)):#For array size
        if i==0:#according initial state to pred
            print('-------------------Round1-------------------')
            REGstate()
            selector=history(initialstate1+initialstate0)
            pred=prediction(select(selector))
            if outcome[0]==pred:
                print('Selector='+history(initialstate1+initialstate0)+',Pred='+pred+',Outcome='+outcome[0]+',Hit')
            else:
                print('Selector='+history(initialstate1+initialstate0)+',Pred='+pred+',Outcome='+outcome[0]+',Miss')
                missrate=missrate+1
            changeREG(history(initialstate0+initialstate1),outcome[0])
        elif i==1:#according initial state to pred
            print('-------------------Round2-------------------')
            REGstate()
            selector=history(initialstate1+outcome[i])
            pred=prediction(select(selector))
            if outcome[1]==pred:
                print('Selector='+history(initialstate1+outcome[i])+',Pred='+pred+',Outcome='+outcome[1]+',Hit')
            else:
                print('Selector='+history(initialstate1+outcome[i])+',Pred='+pred+',Outcome='+outcome[1]+',Miss')
                missrate=missrate+1
            changeREG(history(initialstate1+initialstate0),outcome[1])
        else:
            print('-------------------Round%d-------------------'%(i+1))
            REGstate()
            selector=history(outcome[i-2]+outcome[i-1])
            pred=prediction(select(selector))
            if outcome[i]==pred:
                print('Selector='+history(outcome[i-2]+outcome[i-1])+',Pred='+pred+',Outcome='+outcome[i]+',Hit')
            else:
                print('Selector='+history(outcome[i-2]+outcome[i-1])+',Pred='+pred+',Outcome='+outcome[i]+',Miss')
                missrate=missrate+1
            changeREG(history(outcome[i-2]+outcome[i-1]),outcome[i])
    missrate=missrate/len(outcome)
    print('Misprediction=%f'%missrate)



    f.close()
