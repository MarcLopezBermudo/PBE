import gi
import sys
import threading

gi.require_version("Gtk","3.0")
from gi.repository import Gtk, Gdk, GObject
from pn532_puzzle1 import *

class Finestra(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Puzzle2")
        
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.add(self.box)
        
        self.event_box = Gtk.EventBox()
        self.event_box.override_background_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(0,0,8,1))
        
        self.label = Gtk.Label(label='<span foreground="white" size="x-large">Please, login with your UID</span>')
        self.label.set_use_markup(True)
        self.label.set_size_request(500,200)
        self.event_box.add(self.label)
        
        #self.image = Gtk.Image()
        #self.image.set_from_file('./image_upc.png')
        #self.gtk_image_set_from_icon_name (self.image,NULL,GTK_ICON_SIZE_MENU)
        #self.event_box.add(self.image)
        
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.on_button_clicked)
        
        self.box.pack_start(self.event_box, True, True, 0)
        self.box.pack_start(self.button,True, True, 0)
    
# Funció que es crida un cop premut el botó
    def on_button_clicked(self, widget):
        self.label.set_label('<span foreground="white" size="x-large">Please, login with your UID</span>')
        #self.label.set_use_markup(True)
        self.event_box.override_background_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(0,0,8,1))
        #win = Finestra()
        global thread
        if not thread.isAlive():
            thread = threading.Thread(target=scan_uid)
            thread.start()
        
# Funció que es crida per llegir l'UID amb read_uid 
def scan_uid():
    # Llegim UID
    rf = RfidPnNfc()
    uid = rf.read_uid()
    # Canviem la label a color vermell
    win.label.set_label('<span foreground="white" size="x-large">UID: '+uid+'</span>')
    win.event_box.override_background_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(8,0,0,1))
        
        
if __name__ == "__main__":
    win = Finestra()
    thread = threading.Thread(target=scan_uid)
    # Daemon Threads (non-blocking threads)--> s'executen independentment del thread principal
    #thread.setDaemon(True)
    thread.start()
    win.connect("destroy", Gtk.main_quit)                   
    win.show_all()
    Gtk.main()
        
        
