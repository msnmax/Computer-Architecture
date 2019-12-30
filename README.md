# Computer-Architecture/Project1
## 簡介
* 實作Branch prediction
  * 2-Bit History
* SETUP
  * Environment:WIN10
  * IDE:Pycharm 4.0 Python 3.7
  * Language:Python
### Parameter:
Initial state:
```py    
initialstate0='N'##Initial state
initialstate1='N'#Initial state
```
### Input: 
Eample : N,T,T,N,T,T,N,T,T,N,T,T
### Output: 

`----------------------------Round14----------------------------
[['2C', 'E4', 'E2', 'E8'], ['4C', 'E2', None, None]]
Index=2C,Tag=E8,Hit
[['2C', 'E4', 'E2', 'E8'], ['4C', 'E2', None, None]]
Hit Rate=0.428571`
