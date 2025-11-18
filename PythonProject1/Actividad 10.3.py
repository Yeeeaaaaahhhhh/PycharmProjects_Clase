precios = [1000,2000,3000,4000,5000,6000]

iva = [(lambda x : (x*1.16)) (num)for num in precios ]
print(f''' Precios de los productos + iva son: {(iva)}''')
print("TE HAZ GANADO UN DESCUENTO DEL 30%!!!!!!")
descuento =[(lambda x : (x*0.70)) (num)for num in iva ]
print(f'''El nuevo precio con descuento es {descuento}''')

dolar = [(lambda x : (x/18.34)) (num)for num in descuento ]
euro = [(lambda x : (x/21.45)) (num)for num in descuento ]
print(f'''El costo de estos productos en dolares es: {(dolar)}
El costo de estos productos en euros es {(euro)}''')