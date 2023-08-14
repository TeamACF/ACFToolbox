def regist_fonts(dpg):
    with dpg.font_registry():
        global TopTextFont
        global DefaultButtonFont
        TopTextFont = dpg.add_font("Resources/Fonts/SpaceGrotesk-SemiBold.ttf", 40)
        DefaultButtonFont = dpg.add_font("Resources/Fonts/SpaceGrotesk-SemiBold.ttf", 20)