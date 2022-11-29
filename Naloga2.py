import math

n = int(input("Vnesi število elementov:"))#vnesemo stevilo elementov
l = list() #naredimo list

for i in range(n):
    ele = int(input("Vnesi število:"))#vnesemo stevila
    l.append(ele)

najmanjsi_element = min(l)
najvecji_element = max(l)

vsota_stevil = sum(l)#sestejemo vsa vpisana stevila, da lahko potem izracunamo povprecje
povprecje = vsota_stevil/len(l) #racunanje povprecja

def najblizje_stevilo(l,povprecje): #funkcija za iskanje stevila najblizjega povprecju
    return l[min(range(len(l)), key = lambda i: abs(l[i]-povprecje))]


print ("Najmanjši element je:", najmanjsi_element)
print ("Največji element je:", najvecji_element)
print ("Povprečje števil je:", povprecje)
print ("Najbližje število povprečju je:", najblizje_stevilo(l,povprecje))


