
def smart_func(func):
    def inner(age,mass,long):
        if age<15:
            hel = (long + mass) / 2
            if hel>long:
                return False
            else: return True
        return func(age,mass,long)
    return inner
@smart_func
def healthy(age,mass,long):
    hel=(long+mass)/2
    if hel>long+10:
        return 1
    else:
        return 2
print(healthy(12,23,23))
