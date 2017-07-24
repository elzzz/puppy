import sys
import menu

sys.path.insert(0, '..')
sys.dont_write_bytecode = True

try:
    from lib.config import get_config
except:
    raise


def create_main_window():
    wnd = menu.MainMenu()
    wnd.resize(get_config('../cfg/server.toml')['window']['height'],
               get_config('../cfg/server.toml')['window']['width'])
    wnd.setWindowTitle('MyLovelyServer')

    return wnd
