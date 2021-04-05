from pynfc import Nfc, Timeout

class RfidPnNfc():
  
    def __init__(self):
        self.n = Nfc("pn532_uart:/dev/ttyAMA0:115200")
    # return uid in hexa str
    def read_uid(self):
        for target in self.n.poll():
            try:
                uid = target.uid.decode().upper()
                return uid
            except TimeoutException:
                pass

if __name__ == "__main__":
    print("*** Dipositi el vostre identificador en el lector ***" )
    rf = RfidPnNfc()
    uid = rf.read_uid()
    print('UID: '+ uid)
    print ("*** Welcome! ***")
    
