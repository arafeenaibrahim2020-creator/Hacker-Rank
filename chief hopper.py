def chiefHopper(arr):
    energy=0
    for height in reversed(arr):
        energy=(energy+height+1)//2
    return energy
