import dearpygui.dearpygui as dpg

def start():
    print("Welcome to TEST Module !!!")
    with dpg.window(label="TestModuleWindow") as TestModuleWindow:
        TestModuleWindow_TopText = dpg.add_text("Hey! TestModule Here!",label="TestModuleWindow_TopText")