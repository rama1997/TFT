import os
import cv2

import tft_assets
import tft_functions

class Game:
    def __init__(self, text_queue) -> None:
        self.text_queue = text_queue
        self.gold = ""
        self.current_store = []
        #create dictionary where champ names are the keys
        self.store_count = {}
        for champ in tft_assets.champions:
            self.store_count.update({champ:0})

        self.gameloop()

    def gameloop(self):
        for images in os.listdir("TFT_snapshots"):
            img = cv2.imread("TFT_snapshots/" + images)
            self.gold = str(tft_functions.get_gold(img))
            self.current_store = tft_functions.get_shop_names(img)
            for champ in self.current_store:
                if champ in self.store_count.keys():
                    self.store_count[champ] = self.store_count[champ] + 1
            
        self.update_gui()
        self.gameloop()

    def update_gui(self):
        for champ in self.store_count:
            if self.store_count[champ] > 0:
                self.text_queue.put(champ + ": " + str(self.store_count[champ]))
        
        self.text_queue.put("Current Store: {}".format (', '.join(self.current_store)))
        self.text_queue.put("CURRENT GOLD: " + self.gold)