import dearpygui.dearpygui as dpg
import guitheme
import guiwindow_size_control
import guifonts
import core
import _thread

def startgui():
    core.init_core()

    dpg.create_context()

    guifonts.regist_fonts(dpg)

    dpg.create_viewport()
    dpg.set_viewport_title("ACFToolbox")
    dpg.set_viewport_height(580)
    dpg.set_viewport_width(1000)
    dpg.setup_dearpygui()

    modules = core.find_modules()

    with dpg.window(label="CoreWindow", width=dpg.get_viewport_width(), height=dpg.get_viewport_height(), no_resize=True, no_move=True, no_title_bar=True) as CoreWindow:
        CoreWindow_TopText = dpg.add_text("Anti Computer Forensics Toolbox",label="CoreWindow_TopText")
        dpg.bind_item_font(CoreWindow_TopText,guifonts.TopTextFont)
        with dpg.group(horizontal=True, label="CoreWindowControlButtons"):
            RescanModulesButton = dpg.add_button(label="Rescan Modules", width=150,height=50 , callback=core.rescan_modules)
            dpg.bind_item_font(RescanModulesButton,guifonts.DefaultButtonFont)
            SettingsButton = dpg.add_button(label="Settings", width=150,height=50)
            dpg.bind_item_font(SettingsButton,guifonts.DefaultButtonFont)
            ReloadGUIButton = dpg.add_button(label="Reload GUI", width=150,height=50)
            dpg.bind_item_font(ReloadGUIButton,guifonts.DefaultButtonFont)
        CoreWindow_Modules_Text = dpg.add_text("Modules:",label="CoreWindow_Modules_Text")
        dpg.bind_item_font(CoreWindow_Modules_Text,guifonts.SecTextFont)
        with dpg.group(horizontal=True, label="ModulesViewButtons"):
            for name in modules:
                if(len(name) > 15):
                    ModuleButton = dpg.add_button(label=name, width=250,height=50, callback=core.module_jump)
                    dpg.bind_item_font(ModuleButton,guifonts.DefaultButtonFont)
                elif(len(name) > 22):
                    ModuleButton = dpg.add_button(label=name, width=350,height=50, callback=core.module_jump)
                    dpg.bind_item_font(ModuleButton,guifonts.DefaultButtonFont)
                else:
                    ModuleButton = dpg.add_button(label=name, width=150,height=50, callback=core.module_jump)
                    dpg.bind_item_font(ModuleButton,guifonts.DefaultButtonFont)

    guitheme.init_theme(dpg)
    _thread.start_new_thread( guiwindow_size_control.keepsize, (dpg,CoreWindow) )
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()