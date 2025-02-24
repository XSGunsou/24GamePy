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
    print("ใช้ตัวเลขชุดนี้ทำให้เท่ากับ 24:", numbers)
    return input("พิมพ์วิธีทำ (หรือพิมพ์ '/exit' เพื่อออก): ")


def play_game():
    print("ยินดีต้อนรับสู่เกม 24!")
    print("เป้าหมายของคุณคือการใช้ +, -, *, หรือ / กับตัวเลขที่ให้ทำให้เท่ากับ 24")
    print("คุณสามารถพิมพ์ '/exit' เพื่อออกจากเกมเมื่อไหร่ก็ได้")

    while True:
        numbers = generate_numbers()

        while True:
            user_input = get_user_input(numbers)

            if user_input == "/exit":
                print("แล้วเจอกันใหม่! 😊")
                return

            if check_solution(user_input, numbers):
                print("✔️ โหดมากๆ")
                break
            else:
                print("❌ ลองใหม่อีกรอบ!")


play_game()
