from random import choice
import tools
def get_week():
    return choice(['星期1','星期2','星期3','星期4','星期5','星期6','星期日'])

if __name__ == "__main__":
    print("小專案lesson9_2")
    if tools.OK:
        print(get_week())