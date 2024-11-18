def calculator():
    try:
        user_input = input("Введите операцию (например, '1 + 2'): ")
        parts = user_input.split()


        if len(parts) != 3:
            raise Exception("Ошибка: Неправильный формат. Ожидается (Число_Операция_Число)")

        a = int(parts[0])
        op = parts[1]
        b = int(parts[2])

        if not (1 <= a <= 10 and 1 <= b <= 10):
            raise Exception("Ошибка: Числа должны быть от 1 до 10.")

        if op not in ['+', '-', '*', '/']:
            raise Exception("Ошибка: Операция должна быть одной из: +, -, *, /.")

        if op == '+':
            print(a + b)
        elif op == '-':
            print(a - b)
        elif op == '*':
            print(a * b)
        elif op == '/':
            print(a // b)

    except Exception as e:
        print(f"throws Exception: {e}")

calculator()