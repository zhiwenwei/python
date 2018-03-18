程序名称：选课系统
作者：支文伟

2.需求
角色:学校、学员、课程、讲师
要求:
1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 课程包含，周期，价格，通过学校创建课程
4. 通过学校创建班级， 班级关联课程、讲师
5. 创建学员时，选择学校，关联班级
5. 创建讲师角色时要关联学校，
6. 提供两个角色接口
6.1 学员视图， 可以注册， 交学费， 选择班级，
6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
6.3 管理视图，创建讲师， 创建班级，创建课程
7. 上面的操作产生的数据都通过pickle序列化保存到文件里'''

3.本次作业实现的需求：都实现了作业的基本要求

4.程序运行环境:pycharm 2017.1.2     python解释器版本：Python3.5

5.程序结构
├── bin
│   ├── __init__.py
│   └── start.py          #执行程序
├── conf
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   └── settings.cpython-35.pyc
│   └── settings.py           #配置文件
├── core
│   ├── __init__.py
│   ├── main.py                  #程序主要功能
│   └── __pycache__
│       ├── __init__.cpython-35.pyc
│       └── main.cpython-35.pyc
├── db                        #数据库目录
│   ├── admin
│   │   └── __init__.py
│   ├── classes
│   ├── course
│   ├── course_to_teacher
│   │   └── __init__.py
│   ├── __init__.py
│   ├── school
│   ├── student
│   └── teacher
├── log
│   └── __init__.py
└── README.txt


7.运行测试:
  详情请看图


