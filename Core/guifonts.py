def regist_fonts(dpg):
    with dpg.font_registry():
        global TopTextFont
        global SecTextFont
        global DefaultButtonFont
        global DefaultChineseFont
        global TopTextChineseFont
        global SecTextChineseFont
        TopTextFont = dpg.add_font("Resources/Fonts/SpaceGrotesk-SemiBold.ttf", 40)
        SecTextFont = dpg.add_font("Resources/Fonts/SpaceGrotesk-SemiBold.ttf", 30)
        DefaultButtonFont = dpg.add_font("Resources/Fonts/SpaceGrotesk-SemiBold.ttf", 20)
        """
        加载中文字体会导致严重性能问题, 故暂时禁用
        with dpg.font("Resources/Fonts/SmileySans-Oblique.ttf",20) as DefaultChineseFont:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
        with dpg.font("Resources/Fonts/SmileySans-Oblique.ttf",40) as TopTextChineseFont:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
        with dpg.font("Resources/Fonts/SmileySans-Oblique.ttf",30) as SecTextChineseFont:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Simplified_Common)
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
        """