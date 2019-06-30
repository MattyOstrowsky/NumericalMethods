
def float_binary(number):
    # dzielimy na całkowite i reszte.
    whole, dec = str(number).split(".")
    whole = int(whole)
    dec = '0.' + dec
    dec = float(dec)
    # znak
    if float(number) > 0:
        result = "0"
    else:
        result = "1"

    # Zamiana cześci całkowitej na binarną.
    if bin(whole).lstrip("0b") == '':
        result += '0.'
    else:
        result += bin(whole).lstrip("0b") + "."

    # pętla przerywana gdy liczba zostanie rozłożona do końca.
    dec_binar = []
    dec_list = []
    while True:
        dec *= 2
        if dec in dec_list or dec == 1.0:
            if dec in dec_list:
                result += '('
            elif dec == 1.0:
                dec_binar.append(1)
            break
        else:
            if dec > 1:
                dec_binar.append(1)
                trash, dec = str(dec).split(".")
                dec = '0.' + dec
                dec = float(dec)
            else:
                dec_binar.append(0)

            dec_list.append(dec)
    # składa liczbę binarną.
    for i in dec_binar:
        result += str(i)
    if dec in dec_list:
        result += ')'

    return print(result)

