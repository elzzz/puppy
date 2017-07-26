MENU = "menu"
COMMAND = "command"
EXITMENU = "exitmenu"
PRINT = 'print'

menu_data = {
    'title': "MyLovelyServer",
    'type': MENU,
    'subtitle': "Choose the option, please...",
    'options': [
        {
            'title': 'Show TCP Clients',
            'type': MENU,
            'subtitle': 'Connected Clients List:',
            'options': [
                {
                    'title': 'Show',
                    'type': PRINT
                }
            ]
        },
        {
            'title': 'Send Command To The Client',
            'type': COMMAND,
            'command': 'echo send'
        },
        {
            'title': 'Submenu',
            'type': MENU,
            'subtitle': "Choose the option, please...",
            'options': [
                {
                    'title': 'Say \'Hello\'',
                    'type': COMMAND,
                    'command': 'echo Hello'
                },
                {
                    'title': 'Say \'World\'',
                    'type': COMMAND,
                    'command': 'echo World'
                },
                {
                    'title': 'Say \'Hello World\'',
                    'type': COMMAND,
                    'command': 'echo Hello World'
                },
            ]
        },
        {
            'title': 'Reboot',
            'type': MENU,
            'subtitle': 'Select Yes to Reboot',
            'options': [
                {
                    'title': 'NO',
                    'type': EXITMENU,
                },
                {
                    'title': 'YES',
                    'type': COMMAND,
                    'command': 'echo shutdown'
                },
            ]
        },
    ]
}
