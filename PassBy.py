def PassByValue(x):
    x = ["C"]
    print("Isi variabel x : ", x)
    return x

def PassByReference(x):
    x.append("C")
    print("Isi variabel x : ", x)
    return x

KelasGT = ["A", "B"]

print("KelasGT sebelum run function : ", KelasGT)
PassByValue(KelasGT)
print("KelasGT setelah run function PassByValue : ", KelasGT)
PassByReference(KelasGT)
print("KelasGT setelah run function PassByReference : ", KelasGT)