x, y, z = input("Expression: ").split()
match y:
    case "+":
        print(f"{(float(x) + float(z)):.1f}")
    case "-":
        print(f"{(float(x) - float(z)):.1f}")
    case "*":
        print(f"{(float(x) * float(z)):.1f}")
    case "/":
        print(f"{(float(x) / float(z)):.1f}")
