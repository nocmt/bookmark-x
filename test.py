import json
from requests_html import HTMLSession

session = HTMLSession()

# 检查链接是否可用
dict_obj = {}


def checkUrl(url):
    try:
        if session.get(url).status_code == 200:
            return True
        else:
            return False
    except:
        return False

# 书签失效自检
import os

def decBookmark(filePath=None):
    os.remove('C:/Users/Carl/AppData/Local/Google/Chrome/User Data/Default/Bookmarks.bak')
    filePath = 'C:/Users/Carl/AppData/Local/Google/Chrome/User Data/Default/Bookmarks'
    with open(filePath, 'r+', encoding='utf8') as f:  # 打开json文件
        dict_obj = json.loads(f.read())  # 转成dict
        # 获取书签栏书签
        Bookmark_Bars = dict_obj['roots']['bookmark_bar']['children']
        # 循环获取信息
        for bar in Bookmark_Bars:
            items = bar.get('children')
            if items:
                for item in items:
                    if checkUrl(item['url']):
                        print('It is good')
                    else:
                        name = item['name']
                        print('失效')
                        item['name'] = f'[失效]{name}'
            else:
                item = bar
                print('特殊情况，乱建立书签')
                if not checkUrl(item['url']):
                    name = item['name']
                    item['name'] = f'[失效]{name}'
        f.truncate()
        f.write(json.dumps(dict_obj))


# roots = ['bookmark_bar', 'other', 'synced']

# def checksum_bookmarks(bookmarks):
#     md5 = hashlib.md5()

#     def checksum_node(node):
#         md5.update(node['id'].encode())
#         md5.update(node['name'].encode('utf-16le'))
#         if node['type'] == 'url':
#             md5.update(b'url')
#             md5.update(node['url'].encode())
#         else:
#             md5.update(b'folder')
#             if 'children' in node:
#                 for c in node['children']:
#                     checksum_node(c)

#     for root in roots:
#         checksum_node(bookmarks['roots'][root])
#     return md5.hexdigest()

if __name__ == "__main__":
    decBookmark()
