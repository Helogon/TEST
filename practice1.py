def main():
    # 竖列
    print("I\'m\nNoob")

    # 求平均值
    print("平均值计算器\n请输入数字,完毕后请输入F")
    total = 0
    count = 0
    i = input()
    while i != "F":
        total = total + float(i)
        count = count + 1
        i = input()
    avg = total / count
    if count == 0:
        print(0)
    else:
        print(f"平均值为：{avg}")

    # 输出数字序列
    for i in range(10):
        print(i)

    # 计算矩形面积
    print("请输入矩形的长和宽：")
    a = float(input())
    b = float(input())
    S = a * b
    print(f"矩形的面积为：{S}")

    # 利息计算
    money = float(input("请输入本金金额"))
    nomoney = float(input("请输入最终本息金额"))
    time = int(input("请输入存款时长(年)"))
    interest = (nomoney - money) / (time * money) * 100
    print(f"您的年利率为{interest}%")

    # 比大小
    a = float(input("请输入比大小的数:"))
    b = float(input("请输入比大小的数:"))
    if a > b:
        print(f"{a}>{b}")
    elif a == b:
        print(f"{a}={b}")
    else:
        print(f"{a}<{b}")

    # 最大公约数
    a = int(input("请输入数字:"))
    b = int(input("请输入数字:"))
    list1 = []
    list2 = []
    list3 = []
    for i in range(1, a + 1):
        if a % i == 0:
            list1.append(i)
    for u in range(1, b + 1):
        if b % u == 0:
            list2.append(u)
    if a > b:
        x = a
    else:
        x = b
    for y in range(1, x + 1):
        if y in list1 and y in list2:
            list3.append(y)
    result = max(list3)
    print(f"最大公约数为：{result}")


if __name__ == "__main__":
    main()
