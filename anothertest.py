import MyFirstClass

xxx = MyFirstClass.Complex(2.3, 44)
yyy = MyFirstClass.Complex(222, 4444)


print(xxx.r, xxx.i)

print(yyy.r, yyy.i)


xxx.printsomething('ping')

if xxx.printwasused:
    print('yup, was used')