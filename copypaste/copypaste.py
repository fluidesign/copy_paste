#! python
import pyperclip
import keyRead
import config_manager
import appGui

_running = True


def determine_keystroke():
    charbuffer = keyRead.getcharacter()
    result = keyRead.convertchar(charbuffer) 
    return result


def main():
    global _running
    safe_close_keystroke = config_manager.get_config_value('app-control','safe_close_keystroke')
    open_clipboard_list_keystroke = config_manager.get_config_value('app-control','open_clipboard_list_keystroke')
    save_clipboard_keystroke = config_manager.get_config_value('app-control','save_clipboard_keystroke')

    while _running:
        keystroke = determine_keystroke()
        print(open_clipboard_list_keystroke)
        if keystroke == safe_close_keystroke:
            print("Safe close software captured, closing...")
            _running = False
        elif keystroke == open_clipboard_list_keystroke:
            print("Open clipboard history")
            _appGui = appGui.AppGui()
            _appGui.mainloop()
        elif keystroke == save_clipboard_keystroke:
            print("Clipboard saved")
        else:
            print("key captured " + keystroke)
    
main()