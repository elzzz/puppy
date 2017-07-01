from logbook import FileHandler, Logger
import sys
sys.dont_write_bytecode = True


def get_logger():
    FileHandler('app.log').push_application()
    return Logger('Puppy')
