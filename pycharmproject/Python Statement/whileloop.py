# Handling Errors by Testing Inputs
while True:
    reply=input('enter Text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!'*8)
    else:
        print(int(reply)**2)
    print('Bye')