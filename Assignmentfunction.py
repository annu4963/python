def take_mark():
    nep=input("Enter marks of nepali")
    eng=input("Enter marks of english")
    math=input("Enter marks of maths")
    sci=input("Enter marks of science")
    comp=input("Enter marks of computer")
return take_mark

@take_mark
def total():
    sum=nep+eng+math+sci+comp
    return sum
print(total())
