
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
        self.score_btn = [self.btn_ones, self.btn_twos, self.btn_threes, self.btn_fours, self.btn_fives, self.btn_sixes, self.btn_3same, self.btn_4same, self.btn_fullhouse, self.btn_smstr, self.btn_lgstr, self.btn_yhatzee, self.btn_chance, self.btn_skip]
        self.score_lbl = [self.lbl_ones, self.lbl_twos, self.lbl_threes, self.lbl_fours, self.lbl_fives, self.lbl_sixes, self.lbl_3same, self.lbl_4same, self.lbl_fullhouse, self.lbl_smstr, self.lbl_lgstr, self.lbl_yhatzee, self.lbl_chance]
        self.playable_btns_p1 = [self.btn_ones, self.btn_twos, self.btn_threes, self.btn_fours, self.btn_fives, self.btn_sixes, self.btn_3same, self.btn_4same, self.btn_fullhouse, self.btn_smstr, self.btn_lgstr, self.btn_yhatzee, self.btn_chance]
        self.playable_btns_p2 = [self.btn_ones, self.btn_twos, self.btn_threes, self.btn_fours, self.btn_fives, self.btn_sixes, self.btn_3same, self.btn_4same, self.btn_fullhouse, self.btn_smstr, self.btn_lgstr, self.btn_yhatzee, self.btn_chance]
        self.reset()
        self.btn_done.setDisabled(True)
    
    current_player = "p1"
    dice = [1,1,1,1,1]
    selected_dice = []
    re_rolled = 0
    score_p1 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    score_p2 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    qmode = False
    done_mode = False
    
    def message_box(self,text,title):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(text)
            msg.setWindowTitle(title)
            msg.exec()
    
    def reset(self):
        self.dice = [1,1,1,1,1]
        self.selected_dice = []
        self.playable_btns_p1 = [self.btn_ones, self.btn_twos, self.btn_threes, self.btn_fours, self.btn_fives, self.btn_sixes, self.btn_3same, self.btn_4same, self.btn_fullhouse, self.btn_smstr, self.btn_lgstr, self.btn_yhatzee, self.btn_chance]
        self.p1_yhatzee_first_time = True
        self.playable_btns_p2 = [self.btn_ones, self.btn_twos, self.btn_threes, self.btn_fours, self.btn_fives, self.btn_sixes, self.btn_3same, self.btn_4same, self.btn_fullhouse, self.btn_smstr, self.btn_lgstr, self.btn_yhatzee, self.btn_chance]
        self.p2_yhatzee_first_time = True
        self.re_rolled = 0
        self.update_btn()
        self.btn_roll.setText("Roll")
        self.update_score_lbls()
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
                    self.selected_dice.remove(i)
                    self.sender().setText("")
                    self.sender().setStyleSheet(f"border-image: url(\"images/dice/{self.dice[i]}.png\") 0 0 0 0 stretch stretch;")
    
    def btn_roll_a(self):
        for i in range(len(self.dice_btn)):
            self.dice_btn[i].setDisabled(False)
        self.btn_done.setDisabled(False)
        if self.re_rolled < 3:
            if str(self.sender().text()) == "Roll":
                self.roll_dice("all")
                self.update_btn()
                self.btn_roll.setText("Roll Selected")
                self.re_rolled += 1
            else:
                if len(self.selected_dice) == 0 and str(self.sender().text()) == "Roll Selected":
                    self.message_box("No dice selected","Error")
                else:
                    for i in range(len(self.selected_dice)):
                        self.roll_dice(self.selected_dice[i])
                    for i in range(len(self.dice_btn)):
                        self.dice_btn[i].setText("")
                    
                    self.selected_dice.clear()
                    self.update_btn()
                    self.re_rolled += 1
        else:
            self.message_box("You have already spent all your rolls","Error")
    
    def btn_exit_a(self):
        exit()
    
    def btn_done_a(self):
        self.done_mode = True
        for i in range(len(self.dice_btn)):
            self.dice_btn[i].setDisabled(True)
            self.dice_btn[i].setStyleSheet(f"border-image: url(\"images/dice/{self.dice[i]}.png\") 0 0 0 0 stretch stretch;")
            self.dice_btn[i].setText("")
        for i in range(len(self.score_btn)):
            self.score_btn[i].setDisabled(True)
        self.update_score_lbls()
        self.btn_done.setDisabled(True)
        self.btn_roll.setDisabled(True)
        self.btn_yhatzee.setDisabled(False)
        self.btn_skip.setDisabled(False)
    
    def switch_turn(self):
        if self.current_player == "p1":
            self.current_player = "p2"
            self.lbl_turn.setText("Player 2's Turn")
        elif self.current_player == "p2":
            self.current_player = "p1"
            self.lbl_turn.setText("Player 1's Turn")
        self.btn_roll.setText("Roll")
        self.re_rolled = 0
        self.selected_dice.clear()
        self.dice = [1,1,1,1,1]
        self.update_btn()
        for i in range(len(self.dice_btn)):
            self.dice_btn[i].setDisabled(True)
        for i in range(len(self.score_btn)):
            self.score_btn[i].setDisabled(True)
        self.btn_roll.setDisabled(False)
        self.btn_done.setDisabled(True)
    
    def check_win(self):
        checker = False
        checker2 = False
        if self.current_player == "p1":
            try:
                test = self.score_p1[0]
            except:
                checker = True
        elif self.current_player == "p2":
            try:
                test = self.score_p2[0]
            except:
                checker2 = True
        if checker or checker2:
            score_final_p1 = sum(self.score_p1)
            score_final_p2 = sum(self.score_p2)
            if score_final_p1 > score_final_p2:
                self.message_box("Player 1 wins","Success")
            elif score_final_p2 > score_final_p1:
                self.message_box("Player 2 wins","Success")
            else:
                self.message_box("It's a draw","Success")
            self.message_box('Play again? (If no, just exit after clicking "ok")', "Message")
            self.reset()
    def num_score_btns(self, num, mode = None):
        if mode == "q":
            self.message_box(f"Takes the sum of all the {num} dice present (eg. 3 {num}'s = {num*3}pts)","Help")
        else:
            if self.current_player == "p1":
                for i in range(len(self.dice)):
                    if self.dice[i] == num:
                        self.score_p1[num-1] += num
                self.message_box(f"You scored {self.score_p1[num-1]} points","Success")
                self.playable_btns_p1.remove(self.score_btn[num-1])
            elif self.current_player == "p2":
                for i in range(len(self.dice)):
                    if self.dice[i] == num:
                        self.score_p2[num-1] += num
                self.message_box(f"You scored {self.score_p2[num-1]} points","Success")
                self.playable_btns_p2.remove(self.score_btn[num-1])
            self.end_of_turn()
        
    def update_score_lbls(self):
        if self.current_player == "p1":
            current = self.score_p1
        elif self.current_player == "p2":
            current = self.score_p2
        for i in range(len(current)):
                self.score_lbl[i].setText(str(current[i]))
        if self.current_player == "p1":
            for i in range(len(self.playable_btns_p1)):
                self.playable_btns_p1[i].setDisabled(False)
        elif self.current_player == "p2":
            for i in range(len(self.playable_btns_p2)):
                self.playable_btns_p2[i].setDisabled(False)
            
        
    
    def btn_ones_a(self):
        if self.qmode == True:
            self.num_score_btns(1, "q")
        else:
            self.num_score_btns(1)
    
    def btn_twos_a(self):
        if self.qmode == True:
            self.num_score_btns(2, "q")
        else:
            self.num_score_btns(2)
    
    def btn_threes_a(self):
        if self.qmode == True:
            self.num_score_btns(3, "q")
        else:
            self.num_score_btns(3)
    
    def btn_fours_a(self):
        if self.qmode == True:
            self.num_score_btns(4, "q")
        else:
            self.num_score_btns(4)
    
    def btn_fives_a(self):
        if self.qmode == True:
            self.num_score_btns(5, "q")
        else:
            self.num_score_btns(5)
    
    def btn_sixes_a(self):
        if self.qmode == True:
            self.num_score_btns(6, "q")
        else:
            self.num_score_btns(6)
    
    def same_kind_a(self, num, sender):
        numbers = [0,0,0,0,0]
        str_3 = False
        str_4 = False
        for i in range(len(self.dice)):
            for j in range(len(self.dice)):
                if self.dice[i] == self.dice[j]:
                    numbers[i] += 1 
        numbers = sorted(set(numbers))
        if all(num in numbers for num in [3]) == True:
            str_3 = True
        if all(num in numbers for num in [4]) == True:
            str_4 = True
        
        if sender == self.btn_4same and str_3 == True:
            str_3 = False
            
        if sender == self.btn_3same and str_4 == True:
            str_4 = False
            str_3 = True
        
        if str_3 == True or str_4 == True:
            if self.current_player == "p1":
                if str_3 == True:
                    self.score_p1[6] += self.dice[0] + self.dice[1] + self.dice[2] + self.dice[3] + self.dice[4]
                    self.message_box(f"You scored {self.score_p1[6]} points","Success")
                    self.playable_btns_p1.remove(self.btn_3same)
                elif str_4 == True:
                    self.score_p1[7] += self.dice[0] + self.dice[1] + self.dice[2] + self.dice[3] + self.dice[4]
                    self.message_box(f"You scored {self.score_p1[7]} points","Success")
                    self.playable_btns_p1.remove(self.btn_4same)
            elif self.current_player == "p2":
                if str_3 == True:
                    self.score_p2[6] += self.dice[0] + self.dice[1] + self.dice[2] + self.dice[3] + self.dice[4]
                    self.message_box(f"You scored {self.score_p2[6]} points","Success")
                    self.playable_btns_p2.remove(self.btn_3same)
                elif str_4 == True:
                    self.score_p2[7] += self.dice[0] + self.dice[1] + self.dice[2] + self.dice[3] + self.dice[4]
                    self.message_box(f"You scored {self.score_p2[7]} points","Success")
                    self.playable_btns_p2.remove(self.btn_4same)
            self.end_of_turn()
        else:
            self.message_box(f"You don't have {num} of a kind","Error")
        
        
    
    def btn_3same_a(self):
        if self.qmode == True:
            self.message_box("If there are 3 of the same kind present, you score the sum of all the dice.", "Help")
        else:
            self.same_kind_a(3, self.sender())
        
    def btn_4same_a(self):
        if self.qmode == True:
            self.message_box("If there are 4 of the same kind present, you score the sum of all the dice.", "Help")
        else:
            self.same_kind_a(4, self.sender())
    
    def btn_fullhouse_a(self):
        if self.qmode == True:
            self.message_box("If there are 2 of one kind and 3 of another present, you score 25 points.", "Help")
        else:
            numbers = [0,0,0,0,0]
            checkif = [2,3]
            for i in range(len(self.dice)):
                for j in range(len(self.dice)):
                    if self.dice[i] == self.dice[j]:
                        numbers[i] += 1 
            numbers = sorted(set(numbers))
            if all(num in numbers for num in checkif) == True:
                if self.current_player == "p1":
                    self.score_p1[8] += 25
                    self.message_box(f"You scored {self.score_p1[8]} points","Success")
                    self.playable_btns_p1.remove(self.btn_fullhouse)
                elif self.current_player == "p2":
                    self.score_p2[8] += 25
                    self.message_box(f"You scored {self.score_p2[8]} points","Success")
                    self.playable_btns_p2.remove(self.btn_fullhouse)
                self.end_of_turn()
            else:
                self.message_box(f"You don't have a full house","Error")
        
                    
    def straights(self, sender):
        dice_copy = self.dice
        dice_copy = sorted(set(dice_copy))
        lgstr = dice_copy == [1, 2, 3, 4, 5] or dice_copy == [2, 3, 4, 5, 6]
        smstr = False
        
        if lgstr == False:
            small_straights = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
            for straight in small_straights:
                if all(num in dice_copy for num in straight) == True:
                    smstr = True
        
        if sender == self.btn_smstr and lgstr == True:
            smstr = True
            lgstr = False
            
        if sender == self.btn_lgstr and smstr == True:
            smstr = False
        
        if smstr == True or lgstr == True:           
            if self.current_player == "p1":
                if smstr == True:
                    self.score_p1[9] += 30
                    self.message_box(f"You scored {self.score_p1[9]} points","Success")
                    self.playable_btns_p1.remove(self.btn_smstr)
                elif lgstr == True:
                    self.score_p1[10] += 40
                    self.message_box(f"You scored {self.score_p1[10]} points","Success")
                    self.playable_btns_p1.remove(self.btn_lgstr)
            elif self.current_player == "p2":
                if smstr == True:
                    self.score_p2[9] += 30
                    self.message_box(f"You scored {self.score_p2[9]} points","Success")
                    self.playable_btns_p2.remove(self.btn_smstr)
                elif lgstr == True:
                    self.score_p2[10] += 40
                    self.message_box(f"You scored {self.score_p2[10]} points","Success")
                    self.playable_btns_p2.remove(self.btn_lgstr)
            self.end_of_turn()
        else:
            if sender == self.btn_smstr:
                self.message_box(f"You don't have a small straight","Error")
            else:
                self.message_box(f"You don't have a large straight","Error")
        
        
    
    def btn_smstr_a(self):
        if self.qmode == True:
            self.message_box("If there is a small straight present (any combination of 4 consecutive dice, so 1,2,3,4 , 2,3,4,5 , etc.), you score 30 points.", "Help")
        else:
            self.straights(self.sender())
    def btn_lgstr_a(self):
        if self.qmode == True:
            self.message_box("If there is a large straight present (any combination of 5 consecutive dice, so 1,2,3,4,5 or 2,3,4,5,6), you score 40 points.", "Help")
        else:
            self.straights(self.sender())
    
    def btn_yhatzee_a(self):
        if self.qmode == True:
            self.message_box("If there are 5 of one kind present, you score 50 points. If it is your second yahtzee of the game, you score 100 pts.", "Help")
        else:
            numbers = [0,0,0,0,0]
            for i in range(len(self.dice)):
                for j in range(len(self.dice)):
                    if self.dice[i] == self.dice[j]:
                        numbers[i] += 1
            numbers = sorted(set(numbers))
            if all(num in numbers for num in [5]) == True:
                if self.current_player == "p1":
                    if self.p1_yhatzee_first_time == True:
                        new = 50
                        self.score_p1[11] += 50
                        self.p1_yhatzee_first_time = False
                    else:
                        new = 100
                        self.score_p1[11] += 100
                    self.message_box(f"You scored {new} points","Success")
                    try:
                        self.playable_btns_p1.remove(self.btn_yhatzee)
                    except:
                        pass
                elif self.current_player == "p2":
                    if self.p2_yhatzee_first_time == True:
                        new = 50
                        self.score_p2[11] += 50
                        self.p2_yhatzee_first_time = False
                    else:
                        new = 100
                        self.score_p2[11] += 100
                    self.message_box(f"You scored {new} points","Success")
                    try:
                        self.playable_btns_p2.remove(self.btn_yhatzee)
                    except:
                        pass
                self.end_of_turn()        
            else:
                self.message_box(f"You don't have a Yhatzee","Error")
              
    
    def btn_chance_a(self):
        if self.qmode == True:
            self.message_box("You score the sum of all the dice, regardless of their values.", "Help")
        else:
            if self.current_player == "p1":
                for i in range(len(self.dice)):
                    self.score_p1[12] += self.dice[i]
                self.message_box(f"You scored {self.score_p1[12]} points","Success")
                self.playable_btns_p1.remove(self.btn_chance)
            elif self.current_player == "p2":
                for i in range(len(self.dice)):
                    self.score_p2[12] += self.dice[i]
                self.message_box(f"You scored {self.score_p2[12]} points","Success")
                self.playable_btns_p2.remove(self.btn_chance)
            self.end_of_turn()
    
    def btn_skip_a(self):
        self.message_box("Turn skipped, 0 points earned","Success")
        self.end_of_turn()
            
    
    def end_of_turn(self):
        self.switch_turn()
        self.check_win()
        self.update_score_lbls()
        for i in range(len(self.score_btn)):
            self.score_btn[i].setDisabled(True)
        self.done_mode = False

    def btn_back_a(self):
        manager.widget.setCurrentWidget(manager.screen1)
        manager.widget.resize(1077, 634)
        
    def btn_qmark_a(self):
        if self.qmode == False:
            self.qmode = True 
        else:
            self.qmode = False
        for i in range (len(self.score_btn)):
            self.score_btn[i].setDisabled(not self.qmode)
        for i in range (len(self.dice_btn)):
            self.dice_btn[i].setDisabled(self.qmode)
        self.btn_roll.setDisabled(self.qmode)
        self.btn_done.setDisabled(self.qmode)
        self.btn_back.setDisabled(self.qmode)
        self.btn_skip.setDisabled(True)
        if self.done_mode == True and self.qmode == False:
            self.btn_done_a()