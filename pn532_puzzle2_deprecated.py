import gi
import threading

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk
from pn532_puzzle1 import *


class Window(Gtk.Window):
    def __init__(self):
       #Window
        Gtk.Window.__init__(self,title="Puzzle2")
        self.set_border_width(5)
       
        #Box
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.add(self.box)
        
        #EventBox
        self.event_box = Gtk.EventBox()
        self.event_box.override_background_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(0,0,8,1))
        self.box.pack_start(self.event_box, True, True, 0)
        
        #Label
        self.label = Gtk.Label(label='<span foreground="white" size="x-large">Please, login with your UID</span>')
        self.label.set_use_markup(True)
        self.label.set_size_request(500,200)
        self.event_box.add(self.label)
       
       #Button
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button,True, True, 0)
        
      
    def on_button_clicked(self, widget):
        self.label.set_label('<span foreground="white" size="x-large">Please, login with your UID</span>')
        self.event_box.override_background_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(0,0,8,1))
        global thread
        if not thread.isAlive():
            thread = threading.Thread(target=scan_uid)
            thread.start()
        
def scan_uid():
    # UID
    rf = RfidPnNfc()
    uid = rf.read_uid()
    win.label.set_label('<span foreground="white" size="x-large">UID: '+uid+'</span>')
    win.event_box.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(8,0,0,1))
        
        
if __name__ == "__main__":
    win = Window()
    thread = threading.Thread(target=scan_uid)
    thread.start()
    win.connect("destroy", Gtk.main_quit)                   
    win.show_all()
    Gtk.main()
        
        
