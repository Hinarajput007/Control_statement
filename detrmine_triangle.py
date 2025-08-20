angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))
if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Right Triangle")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("Obtuse Triangle")
    else:
        print("Acute Triangle")
else:
    print("Invalid triangle.")
