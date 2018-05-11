# -*-coding:utf-8-*-
import glob
from collections import OrderedDict
import os
import re

current_path = os.path.abspath(os.path.dirname(__file__))
__author__ = 'Allen Woo'

APPS_PATH = "/home/work/project/osroom/apps"
class MkDoc():
    def __init__(self):
        pass

    def crate_doc(self):
        '''
        Create the API documentation
        '''
        api_md_path = "{}/docs/api".format(current_path)
        if not os.path.exists(api_md_path):
            os.makedirs(api_md_path)

        api_md_path = "{}/index.md".format(api_md_path)
        wf = open(api_md_path, "w")
        api_files =  glob.iglob(r'{}/modules/*/apis/*.py'.format(APPS_PATH))
        n = 1
        docs = []
        for file in api_files:
            of = open(file)
            lines = of.readlines()
            of.close()
            routing = None
            permission = "unlimited"
            login = ""
            func_name = None
            temp_doc = ""
            for line in lines:
                if line.strip():
                    r = re.search(r'''^@.+\.route.*\((['"]{1}(.+)['"]{1}.*methods.*(\[.*\]))\).*''', line)
                    if r:
                        if func_name:
                            doc = OrderedDict()
                            doc["routing"] = routing
                            doc["methods"] = eval(methods)
                            doc["permission"] = permission
                            doc["login"] = login
                            #doc["func_name"] = func_name
                            doc["doc"] = ""

                            str_doc = ""
                            for k, v in doc.items():
                                if k == "doc":
                                    str_doc = "{}\n\n**Request and parameters:**\n\n    {}".format(str_doc,v)
                                else:
                                    str_doc = "{}\n\n**{}**:{}".format(str_doc, k.replace("_"," ").capitalize(), v)
                            docs.append(str_doc)
                            func_name = None
                            permission = "unlimited"
                            temp_doc = ""

                        routing = "/api{}".format(r.groups()[1])
                        methods = r.groups()[2]
                        continue

                    r = re.search(r'''^def\s+(.+)\(.+''', line)
                    if r:
                        if func_name and not temp_doc:
                            routing = None
                            func_name = None
                            temp_doc = ""
                            continue

                    if routing and not func_name:
                        r = re.search(r'''^@osr_login_required.*$''', line)
                        if r:
                            login = "Yes"
                            continue
                        r = re.search(r'''^def\s+(.+)\(.+''', line)
                        if r:
                            func_name = r.groups()[0]
                            continue

                    if routing and not func_name:
                        r = re.search(r'''^@permission_required\(permissions\(\[(.*)\]\).*$''', line)
                        if r:
                            permission = r.groups()[0].replace('"','').replace("'",'')
                            continue

                        r = re.search(r'''^def\s+(.+)\(.+''', line)
                        if r:
                            func_name = r.groups()[0]
                            continue

                    elif func_name and line:

                        r = re.search(r"(.*)'''\s+", line)
                        if not r:
                            r = re.search(r'(.*)"""\s+', line)
                        if r and not temp_doc:
                            temp_doc = "{}{}".format(temp_doc, re.sub(r"'''", "", line).strip(""))
                            continue

                        if r and temp_doc:
                            temp_doc = "{}{}".format(temp_doc, r.groups()[0])

                            methods = eval(methods)
                            doc = OrderedDict()
                            doc["routing"] = routing
                            doc["methods"] = methods
                            doc["permission"] = permission
                            doc["login"] = login
                            #doc["func_name"] = func_name
                            doc["doc"] = temp_doc
                            doc["doc"] = doc["doc"].strip()
                            str_doc = ""
                            for k, v in doc.items():
                                if k == "doc":
                                    str_doc = "{}\n\n**Request and parameters:**\n\n    {}".format(str_doc,v)
                                elif k == "routing":
                                    str_doc = "{}\n\n#### {}".format(str_doc, "-".join(v.split("/")[2:]))
                                    str_doc = "{}\n\n**Api**:{}".format(str_doc, v)
                                else:
                                    str_doc = "{}\n\n**{}**:{}".format(str_doc, k.replace("_"," ").capitalize(), v)
                            str_doc = "{}\n***".format(str_doc)

                            docs.append(str_doc)
                            routing = None
                            func_name = None
                            permission = "unlimited"
                            temp_doc = ""
                        else:
                            temp_doc = "{}{}".format(temp_doc, re.sub(r"'''", "", line).strip(""))


            if n%3 == 0 and docs:
                wf.writelines(docs)
                docs = []
            n += 1
        wf.close()

mkd = MkDoc()
mkd.crate_doc()
