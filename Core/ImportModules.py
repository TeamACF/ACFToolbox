import importlib

def import_module(module, name):
    # 从一个文件路径创建一个模块规范对象
    spec = importlib.util.spec_from_file_location(name, module)
    # 从这个对象创建一个新的模块对象
    module = importlib.util.module_from_spec(spec)
    # 执行模块中的代码
    spec.loader.exec_module(module)
    # 将模块对象赋值给自定义的名称
    globals()[name] = module

    module.start()