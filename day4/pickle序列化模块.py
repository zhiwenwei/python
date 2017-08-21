#coding:utf-8
#Author:Mr Zhi
import pickle
data = {'k1':123,'k2':456}
p_str = pickle.dumps(data)
print(p_str)
pickle.loads()