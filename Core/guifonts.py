def regist_fonts(dpg):
    with dpg.font_registry():
        global TopTextFont
        global SecTextFont
        global DefaultButtonFont
        TopTextFont = dpg.add_font("Resources/Fonts/SpaceGrotesk-SemiBold.ttf", 40)
        SecTextFont = dpg.add_font("Resources/Fonts/SpaceGrotesk-SemiBold.ttf", 30)
        DefaultButtonFont = dpg.add_font("Resources/Fonts/SpaceGrotesk-SemiBold.ttf", 20)