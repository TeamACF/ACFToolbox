import dearpygui.dearpygui as dpg
import guitheme
import guiwindow_size_control
import guifonts
import core
import _thread

dpg.create_context()

guifonts.regist_fonts(dpg)

dpg.create_viewport()
dpg.set_viewport_title("ACFToolbox")
dpg.set_viewport_height(580)
dpg.set_viewport_width(1000)
dpg.setup_dearpygui()

with dpg.window(label="CoreWindow", width=dpg.get_viewport_width(), height=dpg.get_viewport_height(), no_resize=True, no_move=True, no_title_bar=True) as CoreWindow:
    CoreWindow_TopText = dpg.add_text("Anti Computer Forensics Toolbox",label="CoreWindow_TopText")
    dpg.bind_item_font(CoreWindow_TopText,guifonts.TopTextFont)
    with dpg.group(horizontal=True):
        RescanModulesButton = dpg.add_button(label="Rescan Modules", width=150,height=50 , callback=core.rescan_modules)
        dpg.bind_item_font(RescanModulesButton,guifonts.DefaultButtonFont)
        SettingsButton = dpg.add_button(label="Settings", width=150,height=50)
        dpg.bind_item_font(SettingsButton,guifonts.DefaultButtonFont)
        ReloadGUIButton = dpg.add_button(label="Reload GUI", width=150,height=50)
        dpg.bind_item_font(ReloadGUIButton,guifonts.DefaultButtonFont)

guitheme.init_theme(dpg)
_thread.start_new_thread( guiwindow_size_control.keepsize, (dpg,CoreWindow) )
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()