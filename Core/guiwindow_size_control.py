import time

def keepsize(dpg,cw):
    while True:
        dpg.set_item_height(cw,dpg.get_viewport_height())
        dpg.set_item_width(cw,dpg.get_viewport_width())
        time.sleep(0.1)