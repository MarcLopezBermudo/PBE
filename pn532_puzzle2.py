import gi

gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from gi.repository import Gdk
from pn532_puzzle1 import RfidPnNfc
import threading

class Finestra(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Puzzle2")
        self.set_border_width(5)
        
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.add(self.box)
        
    def on_button_clicked(self, widget):
      
    def scan_uid(self):
      
win = Finestra()
win.connect("destroy", Gtk.main_quit)                   
win.show_all()
Gtk.main()
        
