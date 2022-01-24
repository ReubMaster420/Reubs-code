def division(firstnum, secnumb):
    try:
        myAnswer = firstnum//secnumb
        print('Answer', myAnswer)
    except:
        print('Divide by zero')
division(12,3)
division(10,0)