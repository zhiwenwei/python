#coding:utf-8
#Author:Mr Zhi
import xml.etree.cElementTree as ET
tree = ET.parse('xml_test.xml') #打开xml文件并赋值变量
r = tree.getroot() #getroot用于得到xml文档元素
print(r,r.tag)

#遍历xml文档
for child in r:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)
#只遍历year节点
for node in r.iter('year'):
    print(node.tag,node.text)
#修改
for node in r.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('update','yes')
tree.write('xml_test.xml')