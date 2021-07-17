import bluetooth

bd_addr = "98:D3:91:FD:81:D1"
port = 1


def con_bt(self):
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, port))


def disconnect(self):
    self.sock.close()


def on(self):
    data = "A"
    self.sock.send(data)


def connect_bt(self):
    target_name = "HC-06"
    target_address = None

    nearby_devices = bluetooth.discover_devices()

    for bdaddr in nearby_devices:
        if target_name == bluetooth.lookup_name(bdaddr):
            target_address = bdaddr
            break

    if target_address is not None:
        print("found target bluetooth device with address "), target_address
    else:
        print("could not find target bluetooth device nearby")
