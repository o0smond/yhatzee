
# By: Oliver Osmond
# Date: 2025-01-19
# Program Details: Yhatzee

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import manager
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QMessageBox
from gui.page_2_ui import Ui_MainWindow
import random

if __name__ == "__main__":    
    manager.start()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        with manager.image_gui_path():
            self.setupUi(self)
        
        
        self.dice_btn = [self.btn_d1, self.btn_d2, self.btn_d3, self.btn_d4, self.btn_d5]
        self.score_btn = [self.btn_ones, self.btn_twos, self.btn_threes, self.btn_fours, self.btn_fives, self.btn_sixes, self.btn_3same, self.btn_4same, self.btn_fullhouse, self.btn_smstr, self.btn_lgstr, self.btn_yhatzee, self.btn_chance]
        self.reset()
        self.roll_dice("all")
    
    current_player = "p1"
    dice = [1,1,1,1,1]
    selected_dice = []
    re_rolled = 0
    score_p1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    score_p2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    def message_box(self,text,title):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(text)
            msg.setWindowTitle(title)
            msg.exec()
    
    def reset(self):
        self.dice = [1,1,1,1,1]
        self.selected_dice = []
        self.re_rolled = 0
        self.update_btn()
        self.btn_roll.setText("Roll")
        for i in range(len(self.score_btn)):
            self.score_btn[i].setDisabled(True)
        for i in range(len(self.dice_btn)):
            self.dice_btn[i].setText("")
            self.dice_btn[i].setDisabled(True)
    
    def roll_dice(self, mode = -1):
        if mode == "all":
            self.dice.clear()
            for i in range(5):
                self.dice.append(random.randint(1,6))
        else:
            try:
                self.dice[mode] = random.randint(1,6)
            except:
                print("mode not defined")
                
    def update_btn(self):
        for i in range(len(self.dice_btn)):
            self.dice_btn[i].setStyleSheet(f"border-image: url(\"images/dice/{self.dice[i]}.png\") 0 0 0 0 stretch stretch;")
    
    def dice_click_a(self):
        for i in range(len(self.dice_btn)):
            if self.dice_btn[i] == self.sender():
                if str(self.sender().text()) == "":
                    self.selected_dice.append(i)
                    self.sender().setText("x")
                    self.sender().setStyleSheet(f"border-image: url(\"images/dice/{self.dice[i]}_c.png\") 0 0 0 0 stretch stretch;")
                else:
                    self.selected_dice.pop(i)
                    self.sender().setText("")
                    self.sender().setStyleSheet(f"border-image: url(\"images/dice/{self.dice[i]}.png\") 0 0 0 0 stretch stretch;")
    
    def btn_roll_a(self):
        for i in range(len(self.dice_btn)):
            self.dice_btn[i].setDisabled(False)
        if self.re_rolled < 3:
            if str(self.sender().text()) == "Roll":
                self.roll_dice("all")
                self.update_btn()
                self.btn_roll.setText("Roll Selected")
                self.re_rolled += 1
            else:
                if len(self.selected_dice) == 0:
                    self.message_box("No dice selected","Error")
                else:
                    for i in range(len(self.selected_dice)):
                        self.roll_dice(self.selected_dice[i])
                    for i in range(len(self.dice_btn)):
                        self.dice_btn[i].setText("")
                    self.update_btn()
                    self.selected_dice.clear()
                    self.re_rolled += 1
        else:
            self.message_box("You have already spent all your rolls","Error")
    
    def btn_exit_a(self):
        exit()
    
    def btn_done_a(self):
        for i in range(len(self.dice_btn)):
            self.dice_btn[i].setDisabled(True)
            self.dice_btn[i].setStyleSheet(f"border-image: url(\"images/dice/{self.dice[i]}.png\") 0 0 0 0 stretch stretch;")
        for i in range(len(self.score_btn)):
            self.score_btn[i].setDisabled(False)
        self.btn_done.setDisabled(True)
        self.btn_roll.setDisabled(True)
    
    def switch_turn(self):
        if self.current_player == "p1":
            self.current_player = "p2"
            self.btn_turn.setText("Player 2's Turn")
            self.btn_roll.setText("Roll")
            self.re_rolled = 0
            self.selected_dice.clear()
            self.dice = [1,1,1,1,1]
            self.update_btn()
        elif self.current_player == "p2":
            self.current_player = "p1"
    
    def btn_ones_a(self):
        pass
    
    def btn_twos_a(self):
        pass
    
    def btn_threes_a(self):
        pass
    
    def btn_fours_a(self):
        pass
    
    def btn_fives_a(self):
        pass
    
    def btn_sixes_a(self):
        pass
    
    def btn_3same_a(self):
        pass
    
    def btn_4same_a(self):
        pass
    
    def btn_fullhouse_a(self):
        pass
    
    def btn_smstr_a(self):
        pass
    
    def btn_lgstr_a(self):
        pass
    
    def btn_yhatzee_a(self):
        pass
    
    def btn_chance_a(self):
        pass
    
    
    