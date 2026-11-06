# 1-тапсырма: Префикстік кодтар. Фано шарты
# Берілгені: N = 23 символ, хабар = 0110110111
# Кодтар: A=0, B=10, C=110, D=111

def minimum_bits(n):
    """Алфавиттегі n символды біркелкі екілік кодтау үшін бит санын табады."""
    k = 0
    while 2 ** k < n:
        k += 1
    return k


def decode_prefix(message, code):
    """Префикстік кодты солдан оңға қарай декодтайды."""
    decoded = []
    current = ""

    for bit in message:
        current += bit

        if current in code:
            decoded.append(code[current])
            current = ""

    if current:
        raise ValueError("Хабардың соңында толық емес кодтық сөз қалды.")

    return decoded


def main():
    alphabet_size = 23
    message = "0110110111"

    code = {
        "0": "A",
        "10": "B",
        "110": "C",
        "111": "D"
    }

    print("1-ЕСЕП. Біркелкі екілік код")
    k = minimum_bits(alphabet_size)
    print(f"Алфавит көлемі: N = {alphabet_size}")
    print(f"2^{k - 1} = {2 ** (k - 1)} < {alphabet_size} <= 2^{k} = {2 ** k}")
    print(f"Жауабы: әр символға ең аз {k} бит қажет.\n")

    print("2-ЕСЕП. Префикстік кодты декодтау")
    print("Кодтар:", code)
    print("Бастапқы хабар:", message)

    result = decode_prefix(message, code)
    print("Декодтау:", " | ".join(
        next(bits for bits, letter in code.items() if letter == symbol)
        for symbol in result
    ))
    print("Нәтиже:", " ".join(result))


if __name__ == "__main__":
    main()
