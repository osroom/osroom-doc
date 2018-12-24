# -*-coding:utf-8-*-
import codecs
import json
import platform
from os import system

import shutil

import jieba
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

print("Support Chinese search")
# 修改成能匹配的中文
py_v = platform.python_version().split(".")
py_v = ".".join(py_v[0:2])

mkdocs_lun_path = "/home/work/project/venv_doc/lib/python{}/site-packages/mkdocs/contrib/search/templates/search".format(py_v)
shutil.copy('./lunr.js', mkdocs_lun_path)

mkdocs_lun_path = "/home/work/project/venv_doc/lib/python{}/site-packages/mkdocs/contrib/search/templates/".format(py_v)
shutil.copy('./search_index.py', mkdocs_lun_path)

# build
system("mkdocs build")


