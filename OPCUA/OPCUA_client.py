from opcua import Client
import time
import opcua

url = "opc.tcp://192.168.56.1:4840"
client = Client(url)
try:
    while True:
        encrypt = input("Use encryption and signature? y/n  ")
        if encrypt == 'y':
            client.set_security_string("Basic256Sha256,SignAndEncrypt,certificate.der,private-key.pem")
            client.secure_channel_timeout = 10000
            client.session_timeout = 10000
            break
        elif encrypt == 'n':
            break
        else:
            print("Wrong answer. Try again")

    client.connect()
    print("Client connected")
except opcua.ua.uaerrors._base.UaError:
    print("Wrong security mode. Try again")
    exit()

client.load_type_definitions()

root = client.get_root_node()
print("Root node is: ", root)
objects = client.get_objects_node()
print("Objects node is: ", objects)

print("Children of root are: ", root.get_children())

uri = "OPCUA_SERVER"
idx = client.get_namespace_index(uri)

while True:
    try:
        Time = root.get_child(["0:Objects", "{}:Parameters".format(idx), "{}:Time".format(idx)])
        Pressure = root.get_child(["0:Objects", "{}:Parameters".format(idx), "{}:Pressure".format(idx)])
        Temp = root.get_child(["0:Objects", "{}:Parameters".format(idx), "{}:Temperature".format(idx)])
        print("Time: ", Time.get_value())
        print("\tPressure: ", Pressure.get_value())
        print("\tTemperature: ", Temp.get_value())
        time.sleep(2)
    except KeyboardInterrupt:
        print("Closing connection...")
        break

client.disconnect()
print("Connection closed")
