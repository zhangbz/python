#!/usr/bin/env python
# coding=utf-8

#让我们来尝试编写一个ORM（"Object Relational Mapping", 即对象-关系映射）框架
#编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个user类来操作对应的数据库表user ,我们期待他写出这样的代码：
class User(Model):
    #定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

#创建一个实例：
u = User(id = 12345, name = 'zhangbz', email = 'zhangbz.happyhacking@gmail.com', password = 'my-pwd')
#保存到数据库
u.save()
'''其中，父类Model和属性StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如save()全部由metaclass自动完成。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单'''

#现在，我们就按上面的接口来实现该ORM
#首先来定义Field类，它负责保存数据库表的字段名和字段类型:
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_tpye = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

#在Field基础上，进一步定义各种类型Field,比如StringField, IntegerField等等：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')      #super    __init__参数

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
