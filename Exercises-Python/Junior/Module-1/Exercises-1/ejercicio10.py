#Una empresa desea calcular el Retorno sobre la Inversión (ROI) y verificar si la inversión fue rentable (mayor a 1).
ingreso  = float(input("Digite su ingreso: "))
inversion = float(input("Digite su inversion: "))

roi = (ingreso - inversion) / inversion

print("Su ROI es de ", roi)

if(roi > 1):
    print("Su inversion fue rentable")
else:
    print("Su inversion no fue rentable")