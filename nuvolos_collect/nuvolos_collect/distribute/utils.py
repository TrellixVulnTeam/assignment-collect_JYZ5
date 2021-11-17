from datetime import datetime as dt
from pathlib import Path
import re
from nuvolos_collect.logging import clog
from nuvolos_collect.exception import SourceDoesNotExistException, ManifestMissingException
import json
import os
from distutils.dir_util import copy_tree

def do_nothing():
    pass

def read_manifest(source_folder):
    """read_manifest

    Reads the manifest log after the grading has happened and creates the data structure based on which
    graded homeworks are copied back to the handin folder.

    Args:
        source_folder (str): The folder which contains the list of submissions grouped by users.
    """
    
    if not os.path.exists(source_folder):
        raise SourceDoesNotExistException(f"Source {source_folder} does not exist.")
    
    path = f'{source_folder}/nvcollect_manifest.json'
    with open(path, 'r') as j:
        info = json.loads(j.read())
    clog.debug(info)
    return info
    
def generate_target_info(source_info):
    
    cpinfo = source_info['items']
    
    target_list = []
    for d in cpinfo:
        d['handback_target'] = d['src'].replace('/assignments-review/handin','/assignments-review/handback')
        target_list += [d]
    
    clog.debug(target_list)
    return target_list
        
def execute_handback_copy(target_info):

    for d in target_info:
        copy_tree(d['target'], d['handback_target'])