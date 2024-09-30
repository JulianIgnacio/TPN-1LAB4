dias=int(input("ingrese la cantidad de dias: "))
if dias ==30: 
    print("los meses son abril,junio,septiembre y noviembre")
elif dias == 28:
    print("el mes es febrero")
elif dias == 31:
    print("los meses son: enero, marzo, mayo, julio, agosto, octubre y diciembre")
else:
    print("los dias no pertenecen a ningun mes del año")