aclNum = int(input("Cual es el numero IPV4 ACL? "))
if aclNum >= 1 and aclNum <= 99:
    print("Este es un ACL IPV4 estandar.")
elif aclNum >= 100 and aclNum <= 199:
    print("Esta es una ACL IPV4 extendida")
else:
    print("Esta ACL no es ni extendida ni estandar")
    