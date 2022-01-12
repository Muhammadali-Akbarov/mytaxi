from random import choice

def generate_code():
        numbers=list('1234567890')
        password=''
        for i in range(6):
            c = choice([numbers])
            password+=choice(c)
        
        password
        
        return password