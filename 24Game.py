import random


def generate_numbers():
    return [random.randint(1, 9) for _ in range(4)]

def check_solution(user_input, numbers):
    try:
        result = eval(user_input)

        if result == 24:
            return True
        else:
            return False
    except:
        print("ใช้ได้แค่เครื่องหมาย + - * / นะครับ 😊")
        return False


def get_user_input(numbers):
    print("Use these numbers to make 24:", numbers)
    return input("Enter your equation (or type '/exit' to quit): ")


def play_game():
    print("Welcome to the '24 Game'!")
    print("Your goal is to make 24 using +, -, *, or / with the given numbers")
    print("You can type '/exit' anytime to quit")

    while True:
        numbers = generate_numbers()

        while True:
            user_input = get_user_input(numbers)

            if user_input == "/exit":
                print("til next time! 😊")
                return

            if check_solution(user_input, numbers):
                print("✔️ โหดมากๆ")
                break
            else:
                print("❌ ลองใหม่อีกรอบ!")


play_game()