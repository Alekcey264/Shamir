from random import choice, randint
from math import gcd

prime_list = [x for x in range(2, 2**10) if not [t for t in range(2, x) if not x % t]]

while True:
    try:
        m = int(input("Введите число: "))
        break
    except ValueError:
        print("Ошибка! Введите корректное число.")

j = m
print("Message =", m)
temp_list = []
answer_list = []

print(prime_list)
p = choice(prime_list[10:])
while (p - 1) / 2 not in prime_list:
    p = choice(prime_list[10:])
    """
    Условие из протокола Диффи-Хеллмана
    (p - 1) / 2 - простое число
    """

if m >= p:
    while m >= p:
        n = randint(1, p - 1)
        temp_list.append(n)
        m -= (n)
        """
        Разбиваем сообщение на несколько сообщений, меньших p
        """
temp_list.append(m)

print("p =", p)

for item in temp_list:
    print(f"Item = {item}")
    eA, eB, dA, dB = 0, 0, 0, 0
    x1, x2, x3, x4 = 0, 0, 0, 0

    while gcd(eA, p - 1) != 1:
        eA = randint(1, p - 1)
        """
        Ищем ключ шифрования Алисы, с учетом условия:
        НОД(e, p - 1) = 1
        """
    print(f"Encrypt key A for {item} =", eA)

    while gcd(eB, p - 1) != 1:
        eB = randint(1, p - 1)
        """
        Ищем ключ шифрования Боба, с учетом условия:
        НОД(e, p - 1) = 1
        """
    print(f"Encrypt key B for {item} =", eB)

    """
    Имеет смысл сделать перебор значений в один цикл, чтобы избежать повторов?
    """

    while ((dA * eA) % (p - 1) != 1):
        dA = randint(1, p)
        """
        Ищем ключ дешифрования Алисы, с учетом условия:
        dA * eA mod(p - 1) = 1 
        """
    print(f"Decrypt key A for {item} =", dA)

    while ((dB * eB) % (p - 1) != 1):
        dB = randint(1, p)
        """
        Ищем ключ дешифрования Боба, с учетом условия:
        dB * eB mod(p - 1) = 1 
        """
    print(f"Decrypt key B for {item} =", dB)   

    x1 = (item ** eA) % p
    print("Encoded by A =", x1)
    """
    Шифруем ключем Алисы по формуле:
    x1 = m ^ eA mod(p)
    """

    x2 = (x1 ** eB) % p
    print("Encoded by A and B =", x2)
    """
    Шифруем ключем Боба по формуле:
    x2 = x1 ^ eB mod(p)
    """

    x3 = (x2 ** dA) % p
    print("Decoded by A, encoded by B =", x3)
    """
    Дешифруем ключем Алисы по формуле:
    x3 = x2 ^ dA mod(p)
    """

    x4 = (x3 ** dB) % p
    print("Decoded by A and B =", x4)
    """
    Дешифруем ключем Боба по формуле:
    x4 = x2 ^ dB mod(p)
    x4 - итоговое сообщение
    """
    
    print("Are the temp messages the same?", item == x4)
    if item != x4:
        print("False")
        break
    answer_list.append(x4)
    print("-" * 30)

print("Are the messages the same?", j == sum(answer_list))
print(f"Initial message =", j)
print(f"Final message =", sum(answer_list))