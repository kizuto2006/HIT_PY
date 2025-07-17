a = [1,2,3]
b = [1,2,3]
if( a == b ) :
    print("T")
elif ( a != b ) :
    print("F")
elif ( a is b ) :
    print(" a is b ")
elif ( a is not b ) :
    print(" a isn't b ")

c = a 
if( a is c ) :
    print(" okay ")
else :
    print(" nope ")
