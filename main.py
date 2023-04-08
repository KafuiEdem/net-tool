import telnet_me as tn


username = 'edem'
password ='cisco'
ip_addr = "172.16.20.2"
c = tn.Telnet(username=username,password=password,ip_addr=ip_addr)

c.device_login()
# c.send_comand()

# import getpass
# import telnetlib

# HOST = "172.16.20.2"
# user = input("Enter your Username: ")
# password = getpass.getpass()

# tn = telnetlib.Telnet(HOST)

# tn.read_until(b"Username: ")
# tn.write(user.encode('ascii') + b"\n")
# if password:
#     tn.read_until(b"Password: ")
#     tn.write(password.encode('ascii') + b"\n")

# tn.write(b"enable\n")
# tn.write(b"cisco1\n")
# tn.write(b"confi t\n")
# tn.write(b"int loo 0 \n")
# tn.write(b"ip address 10.10.10.1 255.255.255.255 \n")
# tn.write(b"desc my-loopback-network\n")
# tn.write(b"end\n")
# # tn.write(b"ping 10.10.10.1 rep 2000 size 1500 \n")
# tn.write(b"exit\n")
# print(tn.read_all().decode('ascii'))