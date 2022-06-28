import roi_coords
import ocr
import tft_assets

# Returns current gold value
def get_gold(img) -> int:

    # Run OCR to get gold value
    gold = ocr.run_OCR(img, roi_coords.gold_pos, whitelist = "0123456789")

    # Ensures that function always return an integer
    try:
        return int(gold)
    except ValueError:
        return 0

# Returns names of champs in current shop
def get_shop_names(img):
    champs_in_shop = []
    
    # For every name position
    for coord in roi_coords.champ_store_pos:
        # Run OCR to get shop text
        shop_text = ocr.run_OCR(img, coord, whitelist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ").split()

        #  make all detected string uppercase
        shop_text = [i.title() for i in shop_text]

        # For each string obtained from OCR that is not a champ, match it to a champ name if it's similar enough
        for index, text in enumerate(shop_text):
            if text not in tft_assets.champions: 
                champs_in_shop.append(ocr.find_similar_string(text))
            else:
                champs_in_shop.append(text)

    return champs_in_shop