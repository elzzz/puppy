from logbook import FileHandler, Logger


FileHandler('app.log').push_application()
LOG = Logger('Test Logger')
