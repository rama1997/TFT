import cv2
import os

import roi_coords
import ocr
import tft_assets
import tft_functions


def print_info():
	for champ in store_count:
		if store_count[champ] > 2:
			print(f'You could have made a 2-star {champ}! Unlucky!')
		elif store_count[champ] > 8:
			print(f'You could have made a 3-star {champ}! Bruh...')

	for champ in store_count:
		if store_count[champ] > 0:
			print(champ + ": " + str(store_count[champ]))	
	
	print("CURRENT GOLD : " + gold)

# create dictionary where champ names are the keys
store_count = {}
for champ in tft_assets.champions:
    store_count.update({champ:0})
            
for images in os.listdir("TFT_snapshots"):
	img = cv2.imread("TFT_snapshots/" + images)

	# Get champs in shop
	champs_in_shop = tft_functions.get_shop_names(img)

	# Update store count for each champ detected in shop
	for text in champs_in_shop:
		if text in store_count.keys():
			store_count[text] = store_count[text] + 1

	# Get gold value
	gold = str(tft_functions.get_gold(img))

print_info()
