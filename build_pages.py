#!/usr/bin/env python
# -*-coding:utf-8-*-
# @Time : 2017/11/1 ~ 2019/9/1
# @Author : Allen Woo
import codecs
import platform
import os
import re
import shutil
import sys
import yaml
basedir = os.path.abspath(os.path.dirname(__file__))

if len(sys.argv) > 1:
    version = sys.argv[1]
else:
    version = None

# build前
print("Modify the navigation links")
with open("./original_mkdocs.yml") as rf:
    config = rf.read()
config = yaml.load(config)
if not version:
    version = config['version']

site_dir = "osr/{}".format(version)
start_path = '/osroom-doc/osr/{}'.format(version)
print(version)
# 修改nav路径
for v in config["nav"]:
    for k1, v1 in v.items():
        if isinstance(v1, str):
            continue
        for v2 in v1:
            for k3, v3 in v2.items():
                v2[k3] = "/osroom-doc/{}/{}/".format(site_dir, v3.strip("/"))
# 写入新的yml配置
config["docs_dir"] = "docs-{}".format(site_dir.split("/")[-1])
if start_path:
    config["docs_dir"] = "temp_docs"
    config["site_dir"] = site_dir
with codecs.open("./mkdocs.yml", "w", "utf-8") as wf:
    yaml.dump(config, wf, default_flow_style=False, allow_unicode=True)

print("Support Chinese search")
# 修改成能匹配的中文
py_v = platform.python_version_tuple()
py_v = ".".join(py_v[0:2])

venv_path = "{}/lib/python{}/site-packages/mkdocs/contrib/search/templates".format(sys.prefix, py_v)
mkdocs_lun_path = "{}/search".format(venv_path)
shutil.copy('./lunr.js', mkdocs_lun_path)

mkdocs_lun_path = venv_path
shutil.copy('./search_index.py', mkdocs_lun_path)


def replace_str(content):
    r = re.search(r'\]\((?!{})([a-zA-Z0-9\/#_\u4e00-\u9fa5]+)\).*'.format(start_path), content)
    if r:
        rs = r.groups()[0]
        content = content.replace(rs, "{}{}".format(start_path, rs))
        return content
    return None


print("Replace '{}'".format(start_path))
if start_path:
    os.system("cp -r {basedir}/docs-{version} {basedir}/temp_docs".format(basedir=basedir, version=version))
    for root, dirs, files in os.walk('{}/temp_docs'.format(basedir), topdown=False):
        for name in files:
            if not re.match(r".*\.md", name):
                continue
            fp = os.path.join(root, name)
            of = open(fp)
            lines = of.readlines()
            of.close()
            for i, line in enumerate(lines):
                while True:
                    r = replace_str(content=line)
                    if r != None:
                        line = r
                    else:
                        break
                lines[i] = line
            with open(fp, "w") as wf:
                wf.writelines(lines)

# build
print("build...")
os.system("mkdocs build")

if start_path:
    shutil.rmtree("{basedir}/temp_docs".format(basedir=basedir))
