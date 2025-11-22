# By: Oliver Osmond
# Date: 2025-01-19
# Program Details: Yhatzee

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow
from gui.page_1_ui import Ui_MainWindow

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
            self.main_screen = [self.btn_play, self.btn_view, self.lbl_logo]
            self.btn_back.setVisible(False)
            self.txt_instructions.setVisible(False)
        
    def btn_exit_a(self):
        exit()
    
    def btn_play_a(self):
        manager.widget.setCurrentWidget(manager.screen2)
        manager.widget.resize(945, 847)
        
    def btn_view_a(self):
        self.onoff(False, True)
    
    def btn_back_a(self):
        self.onoff(True, False)
    
    def onoff(self, one, two):
        for i in range(3):
            self.main_screen[i].setVisible(one)
        self.btn_back.setVisible(two)
        self.txt_instructions.setVisible(two)
