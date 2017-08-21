#coding:utf-8
#Author:Mr Zhi
#python3.x已经把md5 module移除，要想用md5得用hashlib module,hashlib主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法
import hashlib
a = hashlib.md5()
a.update(b'hello')  #参数必须是byte类型，否则报Unicode-objects must be encoded before hashing错误
a.update('我爱python'.encode(encoding='utf-8')) #有中文要编译成utf8，编译后就是byte类型
print(a.digest())  # 2进制格式hash
print(a.hexdigest())  # 16进制格式hash


##### md5 #####
m = hashlib.md5()
m.update(b'zhiwenwei')
print(m.hexdigest())

##### sha1 #####
hash = hashlib.sha1()
#hash.update('我爱python'.encode('utf-8'))
hash.update(b'zhiwenwei')
print(hash.hexdigest())

##### sha256 #####
hash = hashlib.sha256()
hash.update(b'zhiwenwei')
print('sha56:',hash.hexdigest())

##### sha384 #####
hash = hashlib.sha384()
hash.update(b'admin')
print(hash.hexdigest())

##### sha512 #####
hash = hashlib.sha512()
hash.update(b'admin')
print(hash.hexdigest())

##### hmac #####
import hmac
h = hmac.new(b'admin')
print(h.hexdigest())