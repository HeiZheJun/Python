#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''python变量的命名应遵守如下规则'''
'''必须以下划线或字母开头，后面接任意数量的下划线、字母、数字
python支持Unicode字符，所以汉子等各种非英文字符也可以作为变量名
例如：_ABC、速度点、r_1都是合法的变量名'''
'''变量名区分大小写，ABC和abc不是一个变量'''
'''禁止使用python保留字（关键字），使用python保留字会报错，python保留字有特殊意义'''
'''常用保留字
and   del   For  is  raise  assert  elif  from  lambda   return  break  else  global  bot  try  class  
except  if  or  while  continue  exec  import  pass  with   def  finally   in  print  yield'''

'''除了命名规则外，在python还有些适用规则，应避免变量名使用下面的样式'''
'''前后有下划线的变量名通常都为系统变量，例如：_name_、 _doc_都是系统变量'''
'''以一个下划线开头的变量不能被from**import**语句从模块导入'''
'''以两个下划线开始，结尾没有下划线的变量，如：__abc是本地变量'''