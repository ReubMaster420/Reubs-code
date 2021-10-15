def happy():
    print(' .  . ')
    print('      ')
    print('.    .')
    print(' .... ')

    return
def sad():
    print(' .  . ')
    print('      ')
    print(' .... ')
    print('.    .')
    return
def songli():
    print(' .  . ')
    print('      ')
    print('  ..  ')
    print('..  ..')
    return
    
emotion = input("are you happy or sad")
if emotion == ('happy'):
    happy()
elif emotion == ('sad'):
    sad()
else:
    songli()
