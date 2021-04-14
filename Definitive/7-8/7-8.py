from assgn import *     #Importa la class Assgn del altre document i totes les meves funcions
import math,time
class Tots_Els_Apartats:
    class Set_1:
        """El primer ex"""
        def cub():
            ask = Assgn(Ar2Dict(["x","y","z"],"metres"),conj="en")
            res = 1
            for i in ask.llista: res *= i
            return "{} m^3".format(res)
        def cilindre():
            ask = Assgn(Ar2Dict(["radi","altura"],"metres"),conj="en")
            return "{} m^3".format(((math.pi)*ask.llista[0]**2)*ask.llista[1])
        def con():
            ask = Assgn(Ar2Dict(["radi","altura"],"metres"),conj="en")
            return "{} m^3".format((((math.pi)*ask.llista[0]**2)*ask.llista[1])/3)
        def esfera():
            ask = Assgn(Ar2Dict(["radi"],"metres"),conj="en")
            return "{} m^3".format((math.pi)*(3/4)*(ask.llista[0]**3))
    class Set_2:
        def DifQuadRect():
            obj = Assgn(rang=range(2))
            if obj.llista[0] == obj.llista[1]:
                return "Quadrat"
            else:
                return "Rectangle"
        def roda():
            roda = """                          ██████████████                  
                      ████▒▒▒▒▒▒▓▓▒▒▒▒▒▒████              
                  ████▒▒▒▒██████▒▒██████▒▒▒▒████          
                ██▒▒▒▒████    ██▒▒██    ████▒▒▒▒██        
              ██▒▒████        ██▒▒██        ████▒▒██      
            ██▒▒██▒▒██        ██▒▒██        ██▒▒██▒▒██    
            ██▒▒████▒▒██      ██▒▒██      ██▒▒████▒▒██    
          ██▒▒████████▒▒██    ██▒▒██    ██▒▒████████▒▒██  
          ██▒▒██████  ██▒▒██  ██▒▒██  ██▒▒██  ██████▒▒██  
        ██▒▒████████    ██▒▒████▒▒████▒▒██    ████████▒▒██
        ██▒▒████████████████▒▒██▓▓██▒▒████████████████▒▒██
        ██▒▒██████████████████▓▓▓▓▓▓██████████████████▒▒██
        ██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██
        ██▒▒██████████████████▓▓▓▓▓▓██████████████████▒▒██
        ██▒▒██            ██▒▒██▓▓██▒▒██            ██▒▒██
        ██▒▒██          ██▒▒████▒▒████▒▒██          ██▒▒██
          ██▒▒██      ██▒▒██  ██▒▒██  ██▒▒██      ██▒▒██  
          ██▒▒██    ██▒▒████  ██▒▒██  ████▒▒██    ██▒▒██  
            ██▒▒████▒▒██  ██████████████  ██▒▒████▒▒██    
            ██▒▒██▒▒██      ██████████      ██▒▒██▒▒██    
              ██▒▒████        ██▒▒██        ████▒▒██      
                ██▒▒▒▒████    ██▒▒██    ████▒▒▒▒██        
                  ████▒▒▒▒██████▒▒██████▒▒▒▒████          
                      ████▒▒▒▒▒▒▓▓▒▒▒▒▒▒████              
                          ██████████████                  
        """
            obj = Assgn({0: ("Radi","metres"),1:("Les voltes que dona","voltes")})
            circ = obj.llista[0]*math.pi
            print("\u001b[1m\u001b[4m\u001b[7m ")
            print(roda)
            print("Una roda de "+str(obj.llista[0])+" metres de radi")
            print("recorre "+str(circ*obj.llista[1])+" m\u001b[0m CADA "+str(obj.llista[1])+" voltes que dona")
            return "FET"
        def Ampliacio():
            exec(open("Definitive/7-8/ampliacio.py").read())
        def OddEven():
            inputs = {
                0: ("des d'ón","enter"),
                1: ("fins ón","enter")
            }
            obj = Assgn(inputs)
            llista = obj.llista
            odd = []
            even = []
            print("\n")
            for i in range(int(llista[0]),int(llista[1]+1)):
                if(i%2!=0):
                    odd.append(i)
                else:
                    even.append(i)
            def suma(list):
                t = 0
                for i in list:
                    t += i
                return t
            print("\u001b[1m\u001b[4m\u001b[7mParells ("+str(len(even))+"):"+color.end)
            time.sleep(1)
            print(List2list(even))
            print(color.t.OKBLUE,"=",suma(even),color.end)
            time.sleep(1.4)
            print("\u001b[1m\u001b[4m\u001b[7mImparells ("+str(len(odd))+"):"+color.end)
            time.sleep(1)
            print(List2list(odd))
            print(color.t.OKGREEN,"=",suma(odd),color.end)
            time.sleep(1)
            print("Total:","(","des de:",int(llista[0]),";fins a:",int(llista[1]),")","\nImparells =",suma(odd),"Parells =",suma(even))
            return ""
    class Vuit_1:
        def VelocitatMitjana():
            inputs = Assgn({0:("distancia","metres"),1:("temps","segons")},conj="en")
            res = inputs.llista[0]/inputs.llista[1]
            return "Result = {} m/s".format(res)
        def km2ms():
            res = int(input("Introdueix kmh o ms: "))
            while not(res in (1,2)):
                print(mess.err)
                res = int(input("Introdueix kmh o ms: "))
            if res == 1:
                return "Ans = {} m/s".format(float(input("kmh?"))/3.6)
            else:
                return "Ans = {} km/h".format(float(input("ms?"))*3.6)
        def VelocitatMitjanaCiclista():
            res = Assgn({0:["Distancia","metres"],1:["Velocitat","m/s"]},conj = "en")
        def VelocitatSo():
            return "És supersónic" if int(input("Km/h?(Avió)"))*3.6 >= 340 else "No ho és"
        def DistQueSeparaDosCotxes():
            dic = Ar2Dict(["Cotxe 1","Cotxe 2"],"km/h")
            dic[2] = ("Temps","hores")
            valors = Assgn(dic,conj="en")
            a = valors.llista[0]*valors.llista[2]
            b = valors.llista[1]*valors.llista[2]
            return "Els separa {} km".format(abs(a-b))
    class Vuit_2:
        def MagnitudsDunCircuitElectric():
            dic = {
                0: ("Resitencia","Ohms"),
                1:  ("Intensitat","Ampers"),
                2: ("Tensió","Volts"),
                3: ("Energia","Joules")
            }
            ask = Assgn(dic,conj="en")
        def LleiDOhm():
            intensitat = float(input("Intensitat en milampers: "))
            while not(intensitat in range(1,1001)):
                print(mess.err)
                intensitat = float(input("Intensitat en milampers: "))
            tensio = float(input("Tensió en volts: "))
            while not(tensio in range(2,231)):
                print(mess.err)
                tensio = float(input("Tensió en volts: "))
            return "{} Ohms".format(intensitat/tensio)
        def ResitenciesEnSerie():
            # Resistencies en serie, progamet.
            valors = []                                                                 #Array de tots els casos
            i = 0                                                                       #Comptador de la iteració
            while True:                                                                 #While True, per parar-ho quan vulgui
                i += 1
                res = input("Resitencia {}: ".format(i))
                if not(res):                                                            #Si el input és buit, trenca el while y passa al còdig de baix
                    print("Casos Finalitzat!")
                    break
                else:
                    try:
                        res = float(res)                                                #Si no, passa a comprovar si es pot passar a float
                        if res == 0:
                            print(mess.err)
                            i-= 1
                            continue
                        else:
                            valors.append(abs(res))
                            print(color.t.OKBLUE,List2list(valors,", "),color.end)
                    except:
                        print(mess.err)                                                 #Si no bloquejem la iteració al mateix punt fins que sigui válid
                        i-= 1
                        continue
            #Preguntem què es vol calcular
            ask = input("En paral·lel o en serie?")
            while ask not in ("0","1"):
                print(mess.err)                                                         #mess.err És un missatge d'error
                ask = input("En paral·lel o en serie?")
            if ask == "0":
                resultat = 0
                for i in valors:
                    resultat += 1/i
                resultat = 1/resultat
                return "En paral·lel dona un total de {} Ohms".format(resultat)
            else:
                return "En serie dona un total de {} Ohms".format(sum(valors))
        def BaixConsum():
            obj = Assgn({0:("Intensitat","Ampers"),1:("Consum","Joules")},conj="en")
            res = obj.llista[0]*obj.llista[1]
            if res >= 1000:
                res /= 1000
                return "{} KWh".format(res)
            else:
                return "{} Wh".format(res)
"""
Un indexador de totes les activitats!
"""
def optionsinclass(cls):
    #Indexa totes les dir d'un objecte i les passa per triar una per després retornarla amb getattr com un attr válid.
    method_list = [method for method in dir(cls) if method.startswith('__') is False]
    print("Options in {}: {}{} {}".format(cls.__name__,color.b.blue,List2list(method_list,", "),color.end))
    if len(method_list) < 1: mess.Empty()
    res = int(input("Index? "))
    while not(res in range(len(method_list))):      #Mentres no sigui un valor dintre l'index no serà válid.
        print(mess.err)
        res = int(input("Index? "))
    return getattr(cls,method_list[res])
def classMehtod(cls):
    a = ": "
    if cls.__doc__ != None: a += cls.__doc__
    print(color.b.red,cls.__name__,a,color.end)
    print(optionsinclass(cls)())
classMehtod(optionsinclass(Tots_Els_Apartats))
os.system("pause")