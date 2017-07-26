MENU = 'menu'
COMMAND = 'command'
EXITMENU = 'exitmenu'
PRINT = 'print'

menu_data = {
    'title': 'MyLovelyServer',
    'type': MENU,
    'subtitle': 'Choose the option, please...',
    'options': [
        {
            'title': 'Show TCP Clients',
            'type': MENU,
            'subtitle': 'Connected Clients List:',
            'options': []
        },
        {
            'title': 'Send Command To The Client',
            'type': MENU,
            'subtitle': 'Choose the server, please...',
            'options': []
        },
    ]
}
