from bs4 import BeautifulSoup

html = """
<ul>
    <li><a href="zhangwuji.com">张无忌</a></li>
</ul>
"""

page = BeautifulSoup(html, "html.parser")

page.find()
a = page.find_all("a", attrs={"href": "zhangwuji.com"})
print(a)