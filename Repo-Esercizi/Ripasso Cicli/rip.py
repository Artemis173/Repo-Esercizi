def transform(x: int) -> int:
    if x % 2 == 0:
        x /= 2
    else:
        x*=3
        x-=1
    return x



def calcola_stipendio(ore_lavorate: int) -> float:
    paga_oraria = 10.0
    paga_overtime = 15.0
    
    if ore_lavorate <= 40:
        stipendio = ore_lavorate * 10
    elif ore_lavorate > 40:
        ore_extra = ore_lavorate - 40
        stipendio_extra = ore_extra * 15
        stipendio_40 = 40 * 10
        stipendio = stipendio_40 + stipendio_extra
    return stipendio



def print_seq(): 
    
    print("Sequenza a):")
    for i in range(1, 8):
        print(i)
    print()
    print("Sequenza b):")
    for i in range(3, 24, 5):
        print(i)
    print()
    print("Sequenza c):")
    for i in range(20, -11, -6):
        print(i)
    print()
    print("Sequenza d):")
    for i in range(19, 52, 8):
        print(i)
    return


def integerPower(number, exp):
    result = number
    counter = 1
    
    while counter < exp:
        result *= number
        counter += 1
    
    return result