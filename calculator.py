"""ماشین‌حساب ساده با چهار عملیات اصلی."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("تقسیم بر صفر مجاز نیست")
    return a / b


def calculate(a, operator, b):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    if operator not in operations:
        raise ValueError("عملیات نامعتبر است")
    return operations[operator](a, b)


def main():
    try:
        first = float(input("عدد اول: "))
        operator = input("عملیات (+، -، *، /): ").strip()
        second = float(input("عدد دوم: "))
        print(calculate(first, operator, second))
    except ValueError as error:
        print(f"خطا: {error}")


if __name__ == "__main__":
    main()
