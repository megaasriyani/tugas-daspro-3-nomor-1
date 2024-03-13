data_mahasiswa = {
    'mahasiswa1': 'password1',
    'mahasiswa2': 'password2',
    'mahasiswa3': 'password3',
    'mahasiswa4': 'password4',
    'mahasiswa5': 'password5',
    'mahasiswa6': 'password6',
    'mahasiswa7': 'password7',
    'mahasiswa8': 'password8',
    'mahasiswa9': 'password9',
    'mahasiswa10': 'password10'
}

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in data_mahasiswa and data_mahasiswa[username] == password:
        print("Selamat datang.")
    else:
        print("Data yang dimasukkan salah.")

login()










