height=float(input("enter your height in m: "))
weight=float(input("enter your weight in kg: "))
cal=round(weight/(height**2))
if cal<18.5:
    print(f"Under Weight {cal}")
elif cal<25:
    print(f"Normal Weight {cal}")
elif cal<30:
    print(f"Over Weight {cal}")
elif cal<35:
    print(f"Obese {cal}")
else:
    print(f"Clinically Obese {cal}")            