t=int(input("Ingrese tamaño del vector:"))

vec1=[]
vec2=[]
suma=[]


print("Ingrese datos del vector [1]:")
for i in range (t):
     num=float(input("Ingrese numero:"))
     vec1.append(num)

print("Ingrese datos del vector [2]:")
for i in range (t):
     num=float(input("Ingrese numero:"))
     vec2.append(num)


#suma
print("Suma: ")
for i in range(t):
     suma.append(vec1[i]+vec2[i])
     
print(suma)