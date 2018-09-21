# -*-coding:utf-8-*-
import codecs
import json
from os import system

import yaml

__author__ = "Allen Woo"

# build前
print("Modify the navigation links")
with open("./original_mkdocs.yml") as rf:
    config = rf.read()
config = yaml.load(config)
site_dir = config['site_dir']

# 修改nav路径
for v in config["nav"]:
    for k1,v1 in v.items():
        if isinstance(v1, str):
            continue
        for v2 in v1:
            for k3, v3 in v2.items():
                v2[k3] = "/osroom-doc/{}/{}/".format(site_dir,v3.strip("/"))
# 写入新的yml配置
with codecs.open("./mkdocs.yml","w","utf-8") as wf:
    yaml.dump(config,wf,default_flow_style=False, allow_unicode=True)

# build
system("mkdocs build")
print("Support Chinese search")
# 修改成能匹配的中文
rf = open("./{}/search/search_index.json".format(site_dir))
doc = rf.read()
with codecs.open("./{}/search/search_index.json".format(site_dir),"w","utf-8") as wf:
    wf.write(json.dumps(json.loads(doc),ensure_ascii=False))

