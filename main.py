def calculate_ic(text):
    """
    Calcula o Índice de Coincidência (IC) de um texto.
    """
    text = ''.join(filter(str.isalpha, text)).upper()
    n = len(text)

    if n == 0:
        return 0

    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    ic = sum(count * (count - 1) for count in freq.values()) / (n * (n - 1))
    return ic


def calculate_subtext_ics(text, key_length):
    """
    Calcula o Índice de Coincidência para subtextos de comprimento key_length.
    """
    text = ''.join(filter(str.isalpha, text)).upper()
    subtexts = ['' for _ in range(key_length)]

    # Divida o texto em subtextos baseados na chave
    for i, char in enumerate(text):
        subtexts[i % key_length] += char

    ics = [calculate_ic(subtext) for subtext in subtexts]
    return subtexts, ics


def print_frequent_letters(subtexts):
    """
    Imprime as letras mais frequentes em cada subtexto.
    """
    for i, subtext in enumerate(subtexts):
        freq = {}
        for char in subtext:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        print(f"Letras mais frequentes no subtexto {i + 1}:")
        for letter, count in sorted_freq:
            print(f"  {letter}: {count}")
        print()


def main():
    text = "MFUUPTVACNUPHVTFREOGWEHUKDHXAOTQPKSGSEUSHRAEEEOWMFJCCOWISUAOEGWAHEOSXYETFQRHISVAFEMIRNIPAHQEDAWSTQAEMKRTSPBRCFTGIMIVAKEAOLKSXHEGRGQNRCJAGUOSUDHCMTVLVIBDXGANEUALERNAUEHWBBRGSTWSJNCLTHOTQWEWEODIFEGXAMPTABELVSKTTRAQOTMTVETNWNVEDFAPTXWNBVGGTHOTPCSLERBMCIGHABLODTXAQRQBTRAFMREKMGPSGGNIRSAUELJOSAFOLQAJSFOJYEQRQMXXIBAHOKEHVMCNTIEOTTEZINUETEFSTBEFIYMCBRCMGSVPRGIGSQVEVAGXOTUDLBQASAOAVMFSAFETGIGRCDXZIHEPRXYMNTQDHHEDRKPMSGSAHITUUFTQRGEATMGNLEGFNUEGGRJPVAWESNAKSOYLOETVXMSRUCNMSMBIQRHXEYTQAYPAHNCVXVDBDGADIYEENEMVATUVIEMZBDCPTVADOFIYMCBRGSMEMFNUAZIM"

    key_length = 7

    subtexts, ics = calculate_subtext_ics(text, key_length)

    for i, ic in enumerate(ics):
        print(f"Índice de Coincidência para o subtexto {i + 1}: {ic:.5f}")

    print_frequent_letters(subtexts)


if __name__ == "__main__":
    main()



