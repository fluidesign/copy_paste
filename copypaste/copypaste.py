#! python
import pyperclip
import keyRead
import config_manager
import appGui
import clipboard_manager
import logger
import logging

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

    try:
        logger = logging.getLogger('global_logger')
    except logging.NullHandler as error:
        print ("We are having an issue with the logging module : {err}".format(err=error))

    logger.debug("We are in the {fun} about to start the main loop".format(fun=__name__))
    while _running:
        keystroke = determine_keystroke()
        if keystroke == safe_close_keystroke:
            logger.info("Safe close software captured, closing...")
            _running = False
        elif keystroke == open_clipboard_list_keystroke:
            logger.debug("Open clipboard history")
            clipboard_manager.retreive_values_from_db()
            #_appGui = appGui.AppGui()
            #if _appGui.counter == 1 :
            #    _appGui.mainloop()
            #else:
            #    print("Only single instance is allowed")
        elif keystroke == save_clipboard_keystroke:
            clipboard_manager.catch_clipboard()
        else:
            logger.debug("key captured " + keystroke)

main()