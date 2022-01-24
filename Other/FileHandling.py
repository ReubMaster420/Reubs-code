import pickle


japan =''
thing = ''
with open("practical.txt","r") as whole_file:
    with open("newpractical.txt","w") as new_file:   
        for line in whole_file:
            if line[0:4] == '19.1':    
                thing = '19.1'
            if line[0:4] == '19.2': 
                thing = '19.2'
            if line[0:4] == '20.1':
                thing = '20.1'
            if line[0:4] == '20.2':
                thing = '20.2'
            japan = thing+':'+line
            new_file.write(japan)
            


