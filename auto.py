ascii = """


__          ___  __ _ _                                   
\ \        / (_)/ _(_) |                                  
 \ \  /\  / / _| |_ _| | ____ _ _ __ ___  _ __  _   _ ___ 
  \ \/  \/ / | |  _| | |/ / _` | '_ ` _ \| '_ \| | | / __|
   \  /\  /  | | | | |   < (_| | | | | | | |_) | |_| \__ \
    \/  \/   |_|_| |_|_|\_\__,_|_| |_| |_| .__/ \__,_|___/
                                         | |              
                                         |_|            
========================================================  
Coded By Nor Ahmad
Github = github.com/archive-code
Instagram = instagram.com/norahm4d
Nb: Tools wifi.id kampus generator
========================================================
"""
print (ascii)

nim = input("[+] Masukan Nim :")
print("[--] Tahun registrasi ditambahin angka 2 semisal 2016 = 20162")
thn = input("[+] Masukan tahun registrasi:")
print("[--] TGL LAHIR = 10 MEI 1991 = 10051991")
tgl = input("[+] Masukan tanggal lahir:")
username = (nim+"@wifi.id")
password = (thn+tgl)
print("Result...")
print("=====================================================")
print ("[+] Username:"+username)
print ("[+] Password:"+password)
