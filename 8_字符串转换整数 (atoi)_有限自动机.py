import re
new_res = re.sub(r'[^\u4e00-\u9fa5^a-zA-Z0-9]','','12莫奈油画作品《日出·印象》现存于哪个国家的美术馆dwa。')
new_res = new_res.strip('0123456789')
print(new_res)