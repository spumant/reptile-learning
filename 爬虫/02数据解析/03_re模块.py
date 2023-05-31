import re

# result = re.finditer(r"\d+", "我今年18岁，我有200000000块")
# for item in result:
#     print(item.group())

# result = re.search(r"\d+", "我叫周杰伦，我今年32岁，我的班级是3年2班")
#
# print(result.group())

# obj = re.compile(r"\d+")
# result = obj.findall("我叫周杰伦，我今年32岁，我的班级是3年2班")
# print(result)

s = """
<div class='西游记'><span id='10010'>中国联通</span></div>
<div class='西游记'><span id='10086'>中国移动</span></div>
"""

obj = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")

result = obj.finditer(s)
for item in result:
    id = item.group("id")
    print(id)
    name = item.group("name")
    print(name)
