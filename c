decimal_conversion_option = "2"
binary_conversion_option = "1"

def binary_to_decimal (b):
    b = str (b)
    d = 0
    for i in range (len (b)):
        d = d + int (b [i]) * 2 ** (len (b) - 1 - i)
        # d = d + int (b [len (b) - 1 - i]) * 2 ** i
    return d

def biggest_power_of_2_in (d):
    cpt = 0
    while d > 1:
        d = d // 2
        cpt = cpt + 1
    return cpt

def make_coefficients (powers):
    coefficients = []
    for i in range (max (powers) + 1):
        if i not in powers:
            coefficients.append (0)
        else:
            coefficients.append (1)
    return coefficients
            
def decimal_to_binary (d):
    powers = []
    while d > 0:
        #print ("(d, powers) = " + str ((d, powers)))
        n = biggest_power_of_2_in (d)
        d = d - 2 ** n
        powers.append (n)
    print (powers)
    b = make_coefficients (powers)
    return b

def decimal_conversion_chosen (n):
    return n == decimal_conversion_option

def binary_conversion_chosen (n):
    return n == binary_conversion_option

def display_options ():
    texte = "Que souhaitez-vous faire : \n" \
      + str (binary_conversion_option) \
      + ": convertir un binaire en dÃ©cimal ?\n" \
      + str (decimal_conversion_option) \
      + ": convertir un dÃ©cimal en binaire ?"
    print (texte)

def chose_decimal_or_binary_conversion ():
    display_options ()
    n = input ("FaÃ®tes votre choix: ")
    return n

def chose_decimal_number ():
    d = int (input ("Entrez le nombre dÃ©cimal: "))
    return d

def chose_binary_number ():
    b = input ("Entrez le nombre binaire: ")
    return b

def display_binary (b):
    word = ""
    for elmt in b:
        word = word + str (elmt)
    print (word)

def display_decimal (d):
    print (d)

def main ():
    n = chose_decimal_or_binary_conversion ()
    if decimal_conversion_chosen (n):
        d = chose_decimal_number ()
        b = decimal_to_binary (d)
        display_binary (b)
    elif binary_conversion_chosen (n):
        b = chose_binary_number ()
        d = binary_to_decimal (b)
        display_decimal (d)
    else:
        print ("Vous devez choisir 1 ou 2 ...")
    
main ()
