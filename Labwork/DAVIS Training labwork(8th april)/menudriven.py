import threedshapes

print("Select Shape:")
print("1. Cube")
print("2. Cuboid")
print("3. Cylinder")
print("4. Cone")
print("5. Sphere")

choice = int(input("Enter choice: "))

print("\nSelect Operation:")
print("1. Curved Surface Area")
print("2. Total Surface Area")
print("3. Volume")

op = int(input("Enter operation: "))


# -------- CUBE --------
if choice == 1:
    a = float(input("Enter side: "))
    
    if op == 1:
        print("CSA:", threedshapes.cube_csa(a))
    elif op == 2:
        print("TSA:", threedshapes.cube_tsa(a))
    elif op == 3:
        print("Volume:", threedshapes.cube_volume(a))


# -------- CUBOID --------
elif choice == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    h = float(input("Enter height: "))
    
    if op == 1:
        print("CSA:", threedshapes.cuboid_csa(l, b, h))
    elif op == 2:
        print("TSA:", threedshapes.cuboid_tsa(l, b, h))
    elif op == 3:
        print("Volume:", threedshapes.cuboid_volume(l, b, h))


# -------- CYLINDER --------
elif choice == 3:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    
    if op == 1:
        print("CSA:", threedshapes.cylinder_csa(r, h))
    elif op == 2:
        print("TSA:", threedshapes.cylinder_tsa(r, h))
    elif op == 3:
        print("Volume:", threedshapes.cylinder_volume(r, h))


# -------- CONE --------
elif choice == 4:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    l = float(input("Enter slant height: "))
    
    if op == 1:
        print("CSA:", threedshapes.cone_csa(r, l))
    elif op == 2:
        print("TSA:", threedshapes.cone_tsa(r, l))
    elif op == 3:
        print("Volume:", threedshapes.cone_volume(r, h))


# -------- SPHERE --------
elif choice == 5:
    r = float(input("Enter radius: "))
    
    if op == 1:
        print("CSA:", threedshapes.sphere_csa(r))
    elif op == 3:
        print("Volume:", threedshapes.sphere_volume(r))
    else:
        print("TSA not applicable separately (same as CSA)")


else:
    print("Invalid choice")