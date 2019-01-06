


print("fonksyon = x3 + 2x -4 ")

y = int(input("ilk değer : "))
z = int(input("ikinci değer : "))
kök1 = float(y*y*y + 2*y -4)
kök2 = float(z*z*z + 2*z -4)
print("f( {} ) = 2*{} - 4 = {}".format(y,y,kök1))
print("f( {} ) = 2*{} - 4 = {}".format(z,z,kök2))

if(kök1 * kök2 < 0 ):
    print("f({}) * f({}) < 0 ".format(y,z))
    print("{} - {} aralığında denklemin kökleri vardır. İkinci aşamaya geçilebilir.".format(y,z))
    print("""
    görsel hali:     ***bu aralıkta kök vardır***                  
                    |-------------|--------------|
                   {}             {}             {}
    """.format(y,(y+z)/2,z))
    print("şimdi görselde de görüldüğü gibi 2 parça halinde bakacağız. {} - {} arası ve {} - {} arası..".format(y,(y+z)/2,(y+z)/2,z))
    t =float((y + z) / 2)
    kök3= float(t*t*t +2*t -4)
    print("f({}) = {} , f({}) = {} , f({}) = {}".format(y,kök1,z,kök2,t,kök3))

    if(kök1 * kök2 < 0):
        print("f({}) * f({}) < 0 ".format(y, t))
        b=float((y+t)/2)
        kök4=float(b*b*b +2*b -4)
        print("denklemin {} - {} arasında kökü vardır.".format(y,t))
        print("""
        görsel hali:
                     ***bu aralıkta kök vardır***
                     |--------------|-------------| 
                     {}             {}              {}
                     
        """.format(y,b,t))

        print("f({}) = {} , f({}) = {} , f({}) = {} ".format(y,kök1,b,kök4,t,kök3))

        c = float((y + b) / 2)
        if(kök1 * kök4 < 0):
            print("f({}) * f({}) < 0 ".format(y,c))

            kök5= float(c*c*c + 2*c -4)
            print("denklemin {} - {} arasında kökü vardır.".format(y,c))
            print("""
            görsel hali:
                         ***bu aralıkta kök vardır***
                        |--------------|--------------|
                       {}             {}              {}
            """.format(y,c,b))

            d = float((y + c) / 2)
            kök6=float(d*d*d + 2*d -4)
            print("f({}) = {} , f({}) = {} , f({}) = {} ".format(y, kök1, c, kök5, d, kök6))

            e =(y+d)/2
            kök7=float(e*e*e + 2*e - 4)

            if(kök1 * kök6 < 0):
                print("f({}) * f({}) < 0 ".format(y,d))
                print("denklemin {} -{} arasında kökü vardır..".format(y,d))
                print("""
                görsel hali:
                          ***bu aralıkta kök vardır***
                        |--------------|--------------|
                       {}             {}              {}
                    
                """.format(y,e,d))

            else:
                print("f({}) * f({}) > 0 ".format(d,z))
                print("Denklemin {} - {} arası kökü yoktur.".format(d,z))
                print("""
                görsel hali:
                          **bu aralıkta kök yoktur**
                        |---------------------------| 
                        {}                          {}
                
                """.format(d,z))
         # y = 1 kök1
         # z = 2 kök2
        #t = 3/2 kök3
        #b = 5/4 kök4
        #c = 9/8 kök5
        #d = 17/16 kök6
        #e = 33/32 kök7
        else:
            print("f({}) * f({}) > 0 ".format(c,z))
            print("Denklemin {} - {} arası kökü yoktur.".format(c,z))
            print("""
            görsel hali:
                        **bu aralıkta kök yoktur**  
                       |--------------------------|
                       {}                         {}
            """.format(c,b))

    else:
        print("f({}) * f({}) = > 0 ".format(t, z))
        print("Denklemin {} - {} arası kökü yoktur.".format(t,z))
        print("""
        görsel hali:
                         **bu aralıkta kök yoktur**
                        |---------------------------| 
                        {}                          {}
        
        """.format(y,z))

else:
    print("f({}) * f({}) > 0 ".format(y,z))
    print("{} - {} arası enklemin kökü yoktur.".format(y,z))
