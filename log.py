from logbook import FileHandler, Logger


def get_logger():
    FileHandler('app.log').push_application()
    log = Logger('Puppy')
    return log
