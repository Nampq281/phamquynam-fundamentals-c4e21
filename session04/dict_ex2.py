import pyexcel
from collections import OrderedDict
r1 = {"#": 1,
"Ten": "Huy",
"Muc luong": 25,
"So gio lam": 14,
}
r2 = {"#": 2,
"Ten": "Hoa",
"Muc luong": 20,
"So gio lam": 14,
}
r3 = {"#": 3,
"Ten": "Tam",
"Muc luong": 15,
"So gio lam": 20,
}

bang_luong = [r1, r2, r3]
tong_luong = 0
danh_sach = []

for k in (bang_luong):
    ten = k["Ten"]
    gio = k["So gio lam"]
    muc = k["Muc luong"]
    luong_info = OrderedDict({
        'name': ten,
        'age': gio,
        'level': muc,
    })
    danh_sach.append(luong_info)

print(danh_sach)

pyexcel.save_as(records = danh_sach, dest_file_name = "bangluong.xlsx")
    # print(k["Ten"], ": ", end ="")
    # luong_thang = k["Muc luong"] * k["So gio lam"]
    # print(luong_thang)
    # tong_luong += luong_thang
# print ("Tong luong: ", tong_luong)