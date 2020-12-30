import requests
from bs4 import BeautifulSoup
url = []
for start_value in range(0, 200, 20):
    example = "https://movie.douban.com/subject/{}/comments?start={}&limit=20&status=P&sort=new_score".format(
        "24733428", start_value)
    url.append(example)
for i in range(len(url)):
    print(url[i])
headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
r = []
soup = []
short_comment = []
for i in range(len(url)):
    r.append(requests.get(url[i], headers=headers))
    soup.append(BeautifulSoup(r[i].text, "html.parser"))
    short_comment.append(soup[i].find_all('span', class_='short'))
comment_list = []
for i in range(len(short_comment)):
    for j in range(len(short_comment[i])):
        comment_list.append(short_comment[i][j].string)
filename = 'Soul Comment.txt'
for i in range(len(comment_list)):
    with open(filename, 'a', encoding='utf-8') as file_object:
        file_object.write(str(i + 1) + '. ' + comment_list[i] + '\n\n')