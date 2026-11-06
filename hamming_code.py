# 1-тапсырма: Кедергіге төзімді кодтау. Хэмминг коды
# 1-нұсқа:
# Ақпараттық комбинация: 0100
# Қате берілген разряд: 3

def xor_bits(bits):
    """Биттерді модуль 2 бойынша қосады (XOR)."""
    result = 0
    for bit in bits:
        result ^= bit
    return result


def encode_hamming(data):
    """4 ақпараттық биттен (7,4) Хэмминг кодын құрады.
    Бақылау разрядтары: 1, 2, 4.
    Ақпараттық разрядтар: 3, 5, 6, 7.
    """
    if len(data) != 4 or any(bit not in "01" for bit in data):
        raise ValueError("Ақпараттық комбинация 4 биттен тұруы керек.")

    bits = [0] * 8  # 1-ден 7-ге дейінгі позициялар қолданылады

    # Ақпараттық биттерді орналастыру
    bits[3], bits[5], bits[6], bits[7] = map(int, data)

    # Жұптық бақылау разрядтарын есептеу
    bits[1] = xor_bits([bits[3], bits[5], bits[7]])
    bits[2] = xor_bits([bits[3], bits[6], bits[7]])
    bits[4] = xor_bits([bits[5], bits[6], bits[7]])

    return bits


def calculate_syndrome(bits):
    """Қабылданған 7 бит үшін синдромды есептейді."""
    s1 = xor_bits([bits[1], bits[3], bits[5], bits[7]])
    s2 = xor_bits([bits[2], bits[3], bits[6], bits[7]])
    s4 = xor_bits([bits[4], bits[5], bits[6], bits[7]])

    # Синдром: S = s4s2s1
    syndrome = s4 * 4 + s2 * 2 + s1
    return s1, s2, s4, syndrome


def main():
    data = "0100"
    error_position = 3

    print("1-ЕСЕП. Хэмминг кодын құру")
    print("Ақпараттық комбинация:", data)
    print("Бақылау позициялары: 1, 2, 4")
    print("Ақпараттық позициялар: 3, 5, 6, 7")

    correct = encode_hamming(data)
    correct_word = "".join(str(correct[i]) for i in range(1, 8))

    print(f"a1 = a3 XOR a5 XOR a7 = {correct[3]} XOR {correct[5]} XOR {correct[7]} = {correct[1]}")
    print(f"a2 = a3 XOR a6 XOR a7 = {correct[3]} XOR {correct[6]} XOR {correct[7]} = {correct[2]}")
    print(f"a4 = a5 XOR a6 XOR a7 = {correct[5]} XOR {correct[6]} XOR {correct[7]} = {correct[4]}")
    print("Дұрыс кодтық комбинация C =", correct_word)

    print("\n2-ЕСЕП. 3-разрядтағы қатені анықтау және түзету")
    received = correct.copy()
    received[error_position] ^= 1
    received_word = "".join(str(received[i]) for i in range(1, 8))
    print("Қабылданған комбинация C* =", received_word)

    s1, s2, s4, syndrome = calculate_syndrome(received)
    print(f"E1 = {s1}, E2 = {s2}, E4 = {s4}")
    print(f"Синдром S = E4E2E1 = {s4}{s2}{s1} (екілік)")
    print(f"Синдромның ондық мәні: {syndrome}")

    if 1 <= syndrome <= 7:
        received[syndrome] ^= 1

    corrected_word = "".join(str(received[i]) for i in range(1, 8))
    print(f"{syndrome}-разряд инверсияланды.")
    print("Түзетілген комбинация =", corrected_word)


if __name__ == "__main__":
    main()
