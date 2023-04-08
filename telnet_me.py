import getpass
import telnetlib


class Telnet:
    def __init__(self,username,password,ip_addr) -> None:
        self.username = username
        self.password = password
        self.HOST = ip_addr
        self.tn = telnetlib.Telnet(self.HOST)

        
    
    def show_output(self):
        print(self.tn.read_all().decode('ascii'))

    def send_comand(self,**kwagr):  
        user_input = input("Enter a command: \n")
        self.tn.write(f"{user_input}\n".encode())
        self.tn.write(b"end\n\n\n\n")
        self.tn.write(b"exit\n")
        self.show_output()

    def device_login(self):
        """ 
            This method is to take the username,password and ip address of the 
            device.
            There is a check to see if the password is correct
        
        """
        # self.username = input(f"Enter your Username: {self.username}")
        passwords = getpass.getpass()
        
        self.tn.read_until(b"Username: ")
        self.tn.write(self.username.encode('ascii') + b"\n")
    
        if passwords:
            self.tn.read_until(b"Password: ")
            self.tn.write(passwords.encode('ascii') + b"\n")
       
        self.tn.write(b"enable\n")
       
        self.tn.write(f"{self.password}\n".encode())
        self.send_comand()
           

