import os
import importlib.util
import ImportModules
import dearpygui.dearpygui as dpg

def init_core():
    pass

def rescan_modules():
    print("WIP")

def find_modules():
    modules_path = "./Modules"
    names = os.listdir(modules_path)
    folders = []
    for name in names:
        full_path = os.path.join(modules_path, name)
        if os.path.isdir(full_path):
            folders.append(name)
    return folders

def module_jump(sender):
    module_folder = "./Modules/" + dpg.get_item_label(sender)
    if(os.path.exists(module_folder + "/entry.py") != True):
        print("BAD Module")
    else:
        ImportModules.import_module(module_folder + "/entry.py","Module_" + dpg.get_item_label(sender))