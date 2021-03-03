from pynfc import Nfc, Desfire, Timeout

n = Nfc("pn532_uart:/dev/ttyAMA0:115200")

DESFIRE_DEFAULT_KEY: b'\x00'*8
MIFARE_BLANK_TOKEN = b'xFF'*1024*4

print("*** Dipositi el vostre identificador en el lector ***" )

class RfidPnNfc:
    # return uid in hexa str
    def read_uid(self):
        for target in n.poll():
            try:
                uid = target.uid.decode().upper()
                return uid
            except TimeoutException:
                pass

if __name__ == "__main__":
    rf = RfidPnNfc()
    uid = rf.read_uid()
    print('UID: '+ uid)
    print ('*** Welcome! ***')
    
