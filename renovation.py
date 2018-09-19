# -*-coding:utf-8-*-
import shutil

__author__ = "Allen Woo"

mkdocs_lun_path = "/home/work/project/venv_doc/lib/python3.5/site-packages/mkdocs/contrib/legacy_search/templates/search/lunr.min.js"
try:
    shutil.copy('./lunr.min.js', mkdocs_lun_path)
    print("Success")
except Exception as e:
    print(e)

mkdocs_lun_path = "/home/work/project/venv_doc/lib/python3.4/site-packages/mkdocs/contrib/search/templates/search/lunr.js"
try:
    shutil.copy('./lunr.js', mkdocs_lun_path)
    print("Success")
except Exception as e:
    print(e)