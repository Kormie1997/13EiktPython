#keszitsen python kodot ami beker egy egesz homersekleti erteket es kiirja
#hogy az adott ertekben milyen halmazallapotu a viz.

def homerseklet():
    homersekletC = int(input("Kerek egy homerseklet erteket: "))

    if homersekletC <= 0:
        print("Szilard Halmazallapot.")
    elif homersekletC > 0 and homersekletC < 100:
        print("Folyekony halmazallapot.")
    else:
        print("Legnemu halmazallapot.")
homerseklet()

homersekletC = 0
def homerseklet():
    if homersekletC <= 0:
        return "Szilard Halmazallapot."
    elif homersekletC > 0 and homersekletC < 100:
        return "Folyekony halmazallapot."
    else:
        return "Legnemu halmazallapot."
    
homersekletC = int(input("Kerek egy homerseklet erteket: "))
print(homerseklet())



