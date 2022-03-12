from bmi import BMI


if __name__ == "__main__":
    #print("我是主程式")
    one = BMI(name="robert",height=178,weight=79)
    print(f"{one.name}的bmi是{one.bmi()}")

    two = BMI(name="robert",height=178,weight=79)
    print(f"{two.name}的bmi是{two.bmi()}")

    three = BMI(name="robert",height=178,weight=79)
    print(f"{three.name}的bmi是{three.bmi()}")


