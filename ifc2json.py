#_*_ utf_8

import sys
import ifcopenshell
from ifc_model.project import Project
import os
import logging
import json

def dump(ifc_file,filename=None):
    # if not filename:

    path,name = getPathandName(ifc_file)
    export_file_path = path+"/"+name+".json"
    logging.info('store json to: {}'.format(export_file_path))
    project = Project()
    project.open_ifc(ifc_file)
    data = project.to_json()
    json.dump(
        data,
        open(export_file_path,'w+'),
        indent=2,
        sort_keys=True
        )
    return project,export_file_path

def getPathandName(file):
    parent_path = os.path.dirname(os.path.abspath(file))
    print('file path = %s' % parent_path)
    file_name = os.path.split(file)[-1]
    print('file name = %s' % file_name)
    return parent_path,file_name


if __name__ == "__main__":
    ifc_file = sys.argv[1];
    dump(ifc_file)
