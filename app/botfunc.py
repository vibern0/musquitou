
def bot_process_message(command):
    response = 'I cant understand!'
    if command.startswith('hi'):
        response = 'hi friend'

    return response
