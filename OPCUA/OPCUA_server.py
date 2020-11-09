from opcua import Server
from random import randint
import datetime
import time
from opcua import ua

server = Server()

url = "opc.tcp://192.168.56.1:4840"
server.set_endpoint(url)

while True:
    encrypt = input("Use encryption and signature? y/n  ")
    if encrypt == 'y':
        server.set_security_policy([ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt])
        server.load_certificate("certificate.der")
        server.load_private_key("private-key.pem")
        break
    elif encrypt == 'n':
        break
    else:
        print("Wrong answer. Try again")

name = "OPCUA_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

server.start()
print("Server started at {}".format(url))

while True:
    Temperature = randint(10, 50)
    Pressure = randint(200, 999)
    T = datetime.datetime.now()

    print(Temperature, Pressure, T)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(T)

    time.sleep(2)
