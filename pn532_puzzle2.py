import gi
import threading

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk,GdkPixbuf
from pn532_puzzle1 import *

class Window(Gtk.Window):
    def __init__(self):
        # Window
        Gtk.Window.__init__(self,title="Puzzle2", decorated=True, name="Window")
        self.set_default_size(500, 200)ç
        
        # Box
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20,name="Box")
        self.add(self.box)
        
        # UPC Image
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename="image_upc.jpg", 
            width=40, 
            height=40, 
            preserve_aspect_ratio=True)   
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        self.box.add(image)

        #Label
        self.label = Gtk.Label(label='Please, login with your UID',name ="Label")
        self.label.set_size_request(500,200)
        self.box.add(self.label)
       
        # Button
        self.button = Gtk.Button(label="Clear",name="Button")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button,True, True, 0)
        
    def on_button_clicked(self, widget):
        self.label.set_label('Please, login with your UID')
        #Thread
        global thread
        if not thread.isAlive():
            thread = threading.Thread(target=scan_uid)
            thread.start()
        
def scan_uid():
    # UID
    rf = RfidPnNfc()
    uid = rf.read_uid()
    win.label.set_label('UID: '+uid)
      
def load_css(self):
    # CSS 
    self.style_provider = Gtk.CssProvider()
    css_file = open("style.css","r")
    css = css_file.read()
    self.style_provider.load_from_data(bytes(css.encode()))
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(), self.style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
    
if __name__ == "__main__":
    win = Window()
    load_css(win)
    thread = threading.Thread(target=scan_uid)
    thread.start()
    win.connect("destroy", Gtk.main_quit)                   
    win.show_all()
    Gtk.main()
        
        
        
