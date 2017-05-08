from logbook import FileHandler, Logger


def get_logger():
    FileHandler('app.log').push_application()
    LOG = Logger('Puppy')
    return LOG
