
#ini adalah nama_variabel kosong
nama_variabel = []
print(nama_variabel)


# list2 = ["alex", "john", "morph"]
# print(list2)


# #ini adalah list berisi integer
# list3 = [1,2,3,4,5,6,7,8,9]
# print(list3)


# list4 = [["a","b","c","d"], 50,"namaku"]
# print(list4)

# list5 = [1,2,3,4,5,6,7,8,9,10]
# print("Hasil dari print list5[2] =  ",list5[2])
# print("Hasil dari negatif indexs [-3] =  ", list5[-3])
# print("range indeks 1:5 =", list5[1:5])





# list6 = [1,2,3,4,5,6,7,8,9,10]
# # #mengubah data pada list
# print(list6)
# list6[9] = "Yaumil"
# print(list6)

# # #cara menghapus satu data pada list
# del list6[9]
# print(list6)

# # #menghapus semua data pada list
# list6.clear()
# print(list6)


# #menambah data pada list
# list6.append("desktop")
# print(list6)

# #menambah banyak data pada list
# list6.extend(["Programing","amcc","2020/2021"])
# print(list6)


# ================Membuat tupple================

# #tuple dengan satu elemen
# my_tuple = (1,)
# print(my_tuple)

# #tuple berisi integer
# my_tuple2 = (1,2,3)
# print(my_tuple2)

# #tuple bersarang
# my_tuple3 = ("hello", [1,2,3])
# print(my_tuple3)

# #tuple dengan tidak menggunakan tanda()
# my_tuple4 = 1,2,3
# print(my_tuple4)

# #tuple dengan memasukan anggota tuple ke variabel yang bersesuaian
# my_tuple5 = 1,2,3
# a, b, c = my_tuple5
# print(a, b, c)

# my_tuple6 = ('Hallo beb')
# print(my_tuple6[1])

# print(my_tuple6[-1])

# print(my_tuple6[:5])

# print(my_tuple6[5:])

# print(my_tuple6[2:5])


# =======mengubah tuple =====

# my_tuple7 = (1,2,3,[6,5])

# print(my_tuple7)
# my_tuple7[3][0] = 4
# print(my_tuple7)

# my_tuple7.clear()
# print(my_tuple7)

# del my_tuple7
# print(my_tuple7)


# tuple8 = ('Hai sayang')
# print(tuple8.count('a'))
# print(tuple8.index('y'))

#set

# set1 = {1,2,3,4,5}
# print(set1)

# list1 = ['a','b','c','d']
# list2 = [1,2,3,4,5]
# set1 = set(list1)
# set2 = set(list2)
# print(set1)
# print(set2)

# set4 = {100,200,300,400,500}
# print(set4)

# #penambahan data tunggal
# set4.add(600)
# print(set4)

# #penambahan banyak data
# set4.update([700,800,900])
# print(set4)

# #menghapus keseluruhan set
# set4.clear()
# print(set4)

# #operasi himpunan matematika
# set4 = {10,20,30,40,50}
# set5 = {50,60,70,80,90}

# print(set4 | set5)
# print(set5.union(set4))

#DICTIONARY
dec1 = {"yk":"Yogyakarta", "jkt":"Jakarta"}
print("Hai namaku yaumil aku asalnya ", dec1["yk"])
print("Hai namaku aksah aku asalnya ", dec1["jkt"])

#Tambah dictionary
dec1["mgl"] = "Magelang"
print(dec1)

#ganti value dict
dec1["mgl"] = "malang"
print(dec1)

del dec1["mgl"]
print(dec1)
dec1["mgl"].clear()
print(dec1)



