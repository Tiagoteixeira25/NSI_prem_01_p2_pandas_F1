decimal_conversion_option = 1
binary_conversion_option = 2

def binary_to_decimal (b):
    b = str (b)
    d = 0
    for i in range (len (b)):
        d = d + int (b [i]) * 2 ** (len (b) - 1 - i)
        d = d + int (b [len (b) - 1 - i]) * 2 ** i
    return d
def power_of_2():
    cpt = 0
    while d > 1:
        d = d//2
        cpt = cpt + 1
    return cpt
def make_coef(powers):
    for i in reversed (range(max(powers)+ 1)):
        if i not in powers:
            coef.append(0)
        else:
            coef.append(1)
        return coef
def decimal_to_binary (d):
    powers = []
    while d >= 0:
        d = d -2**power_of_two(d)
        powers.append (powers_of_two(d))
    coefs = make_coef(powers)
    return b


def decimal_conversion_chosen (n):
    return n == decimal_conversion_option

def binary_conversion_chosen (n):
    return n == binary_conversion_option

def display_options ():
    texte = "Que souhaitez-vous faire : \n" \
      + str (binary_conversion_option) \
      + ": convertir un binaire en decimal ?\n" \
      + str (decimal_conversion_option) \
      + ": convertir un binaire en decimal ?"

def chose_decimal_or_binary_conversion ():
    display_options ()
    n = input ("Faites votre choix: ")
    return n

def chose_decimal_number ():
    d = input ("Entrez le nombre decimal: ")
    return d

def chose_binary_number ():
    b = input ("Entrez le nombre binaire: ")
    return b

def display_binary (b):
    return b

def display_decimal (d):
    return d

def main ():
    n = chose_decimal_or_binary_conversion ()
    if decimal_conversion_chosen (n):
        d = chose_decimal_number ()
        b = decimal_to_binary (d)
        display_binary (b)
    elif binary_conversion_chosen (n):
        b = chose_binary_number ()
        d = binary_to_decimal (b)
        display_decimal (b)
    else:
        print ("Vous devez choisir 1 ou 2 ...")
