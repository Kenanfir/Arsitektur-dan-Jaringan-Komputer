def PassByValue(x):                 # Function dimana variabel x mengambil isi dari variabel KelasGT
    x = ["C"]                       # x membuat variabel baru
    print("Isi variabel x : ", x)   # Check isi variabel x
    return x                        # Pembatas function

def PassByReference(x):             # Function dimana variabel x mengambill isi dari variabel KelasGT dan menambahkan variabel x ke dalamnya
    x.append("C")                   # x menggabungkan "C" kedalam KelasGT dan x itu sendiri karena x dan KelasGT merupakan variabel yang sama
    print("Isi variabel x : ", x)   # Check isi variabel x
    return x                        # Pembatas function

KelasGT = ["A", "B"]                # Contoh variabel

print("KelasGT sebelum run function : ", KelasGT)
PassByValue(KelasGT)                                                   # Run function PassByValue dengan variabel KelasGT
print("KelasGT setelah run function PassByValue : ", KelasGT)
PassByReference(KelasGT)                                               # Run function PassByReference dengan variabel KelasGT
print("KelasGT setelah run function PassByReference : ", KelasGT)
