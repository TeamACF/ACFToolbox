import dearpygui.dearpygui as dpg

def default_ok_callback(sender):
    del1 = dpg.get_item_user_data(sender)[0]
    del2 = dpg.get_item_user_data(sender)[2]
    dpg.delete_item(del1)
    dpg.delete_item(del2)

def default_cancel_callback(sender):
    del1 = dpg.get_item_user_data(sender)[0]
    del2 = dpg.get_item_user_data(sender)[2]
    dpg.delete_item(del1)
    dpg.delete_item(del2)

def show_info(title, message, show_cancel = False, ok_selection_callback = None, cancel_selection_callback = None):

    # guarantee these commands happen in the same frame
    with dpg.mutex() as mutex_id:

        viewport_width = dpg.get_viewport_client_width()
        viewport_height = dpg.get_viewport_client_height()

        with dpg.window(label=title, modal=True, no_close=True) as modal_id:
            dpg.add_text(message)
            if(ok_selection_callback == None):
                dpg.add_button(label="Ok", width=75, user_data=[modal_id, True, mutex_id], callback=default_ok_callback)
            else:
                dpg.add_button(label="Ok", width=75, user_data=[modal_id, True, mutex_id], callback=ok_selection_callback)
            dpg.add_same_line()
            if(show_cancel):
                if(cancel_selection_callback == None):
                    dpg.add_button(label="Cancel", width=75, user_data=[modal_id, False, mutex_id], callback=default_cancel_callback)
                else:
                    dpg.add_button(label="Cancel", width=75, user_data=[modal_id, False, mutex_id], callback=cancel_selection_callback)

    # guarantee these commands happen in another frame
    dpg.split_frame()
    width = dpg.get_item_width(modal_id)
    height = dpg.get_item_height(modal_id)
    dpg.set_item_pos(modal_id, [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2])