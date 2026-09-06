import itertools
import sys
import time

def print_dolphin_banner():
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    # Cessna 150 Full Exterior Side Profile ASCII Art
    SmokeGuy= f"""{CYAN}
                                                          .... NO! ...                  ... MNO! ...
                                                        ..... MNO!! ...................... MNNOO! ...
                                                      ..... MMNO! ......................... MNNOO!! .
                                                     .... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
                                                      ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
                                                         ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
                                                        ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
                                                        ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
                                                         ....... MMMMM..    OPPMMP    .,OMI! ....
                                                          ...... MMMM::   o.,OPMP,.o   ::I!! ...
                                                              .... NNM:::.,,OOPM!P,.::::!! ....
                                                               .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
                                                              ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
                                                                .. MMMMMNNOOMMNNIIIPPPOO!! ......
                                                               ...... MMMONNMMNNNIIIOO!..........
                                                            ....... MN MOMMMNNNIIIIIO! OO ..........
                                                         ......... MNO! IiiiiiiiiiiiI OOOO ...........
                                                       ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
                                                        .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
                                                        ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
                                                           ...... OO! ................. ON! .......
                                                              ................................


                                                          /$$$$$$  /$$   /$$ /$$   /$$  /$$$$$$       /$$
                                                         /$$__  $$| $$  | $$| $$$ | $$ /$$__  $$     | $$
                                                        | $$  \__/| $$  | $$| $$$$| $$| $$  \__/     | $$
                                                        | $$ /$$$$| $$  | $$| $$ $$ $$| $$ /$$$$     | $$
                                                        | $$|_  $$| $$  | $$| $$  $$$$| $$|_  $$     |__/
                                                        | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$     
                                                        |  $$$$$$/|  $$$$$$/| $$ \  $$|  $$$$$$/.     /$$
                                                         \______/  \______/ |__/  \__/ \______/      |__/
                                        
                                        
                                                             
 
    """

    def type_text(text, delay=0.012):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    sys.stdout.write("\033[H\033[J")
    print(SmokeGuy)

    title = f"{BOLD}{CYAN}[+] SmokeGuy Target Dictionary Generator{RESET}\n"
    type_text(title, delay=0.01)

    subtitle = f"{BLUE}[i] Smoke check complete. Ready to build your wordlist.{RESET}"
    type_text(subtitle, delay=0.008)
    print("=" * 65 + "\n")
def get_inputs():
    print_dolphin_banner()
    print("[i] If there is no answer to any question, simply press Enter:\n")
 
    questions = [
        ("first_name", "1. Target's first name: "),
        ("last_name", "2. Target's last name: "),
        ("middle_name", "3. Target's middle name / patronymic: "),
        ("nickname", "4. Main nickname / handle: "),
        ("alt_nickname", "5. Alternate / Old username: "),
        ("dob_day", "6. Day of birth (DD, e.g., 05): "),
        ("dob_month", "7. Month of birth (MM, e.g., 08): "),
        ("dob_year_full", "8. Year of birth (YYYY, e.g., 1995): "),
        ("dob_year_short", "9. Last 2 digits of birth year (YY, e.g., 95): "),
        ("birth_city", "10. Place of birth / City: "),
        ("current_city", "11. Current city of residence: "),
        ("zip_code", "12. Postal / ZIP code: "),
        ("phone_last4", "13. Last 4 digits of phone number: "),
        ("phone_full", "14. Full phone number (without +): "),
        ("id_passport_num", "15. Passport or ID card number (digits): "),

        ("partner_first_name", "16. Partner's / Spouse's first name: "),
        ("partner_last_name", "17. Partner's last name: "),
        ("partner_nickname", "18. Partner's nickname: "),
        ("partner_dob_day", "19. Partner's birth day (DD): "),
        ("partner_dob_month", "20. Partner's birth month (MM): "),
        ("partner_dob_year", "21. Partner's birth year (YYYY): "),
        ("anniversary_day", "22. Relationship / Wedding anniversary day (DD): "),
        ("anniversary_month", "23. Relationship / Wedding anniversary month (MM): "),
        ("anniversary_year", "24. Relationship / Wedding anniversary year (YYYY): "),
        ("first_date_place", "25. Place where they met / First date location: "),

        ("child1_name", "26. First child's first name: "),
        ("child1_nickname", "27. First child's nickname: "),
        ("child1_dob_year", "28. First child's birth year: "),
        ("child2_name", "29. Second child's first name: "),
        ("child2_dob_year", "30. Second child's birth year: "),
        ("child3_name", "31. Third child's name: "),
        ("mother_first_name", "32. Mother's first name: "),
        ("mother_maiden_name", "33. Mother's maiden name: "),
        ("father_first_name", "34. Father's first name: "),
        ("sibling1_name", "35. Brother's / Sister's name: "),
        ("sibling2_name", "36. Second sibling's name: "),
        ("best_friend_name", "37. Best friend's name: "),
        ("godfather_name", "38. Godfather's / Relative's name: "),

        ("pet1_name", "39. First pet's name: "),
        ("pet1_type", "40. First pet's type (e.g., dog, cat): "),
        ("pet1_dob_year", "41. First pet's birth year: "),
        ("pet2_name", "42. Second pet's name: "),
        ("pet2_type", "43. Second pet's type: "),
        ("childhood_pet", "44. Childhood pet's name: "),
        ("favorite_animal", "45. Favorite animal: "),
        ("favorite_dog_breed", "46. Favorite dog/cat breed: "),
        ("aquarium_fish_name", "47. Fish / Other pet's name: "),
        ("exotic_pet", "48. Any other pet/animal name: "),

        ("car_make", "49. Car make (e.g., Toyota, BMW): "),
        ("car_model", "50. Car model (e.g., Camry, E46): "),
        ("car_color", "51. Car color: "),
        ("car_plate_numbers", "52. Digits of car license plate: "),
        ("car_plate_letters", "53. Letters of car license plate: "),
        ("dream_car", "54. Dream car: "),
        ("motorcycle_model", "55. Motorcycle / Scooter model: "),
        ("first_car", "56. First car ever owned: "),
        ("favorite_brand_car", "57. Favorite car brand: "),
        ("car_nickname", "58. Car's nickname: "),

        ("hobby1", "59. Primary hobby: "),
        ("hobby2", "60. Secondary hobby: "),
        ("fav_sport", "61. Favorite sport: "),
        ("fav_team", "62. Favorite sports team: "),
        ("fav_player", "63. Favorite athlete / player: "),
        ("fav_game1", "64. Primary favorite video game: "),
        ("fav_game2", "65. Secondary favorite video game: "),
        ("gaming_tag", "66. In-game nickname / GamerTag: "),
        ("fav_band", "67. Favorite music band / singer: "),
        ("fav_song", "68. Favorite song name: "),
        ("fav_movie", "69. Favorite movie / TV show: "),
        ("fav_actor", "70. Favorite actor / celebrity: "),

        ("primary_school", "71. Primary school number / name: "),
        ("high_school", "72. High school name: "),
        ("university_name", "73. University / College name: "),
        ("degree_major", "74. Field of study / Major: "),
        ("company_name", "75. Workplace / Company name: "),
        ("job_title", "76. Job title / Position: "),
        ("first_job_company", "77. First job / Workplace: "),
        ("street_name", "78. Street name of residence: "),
        ("house_apt_num", "79. House or Apartment number: "),
        ("favorite_vacation_spot", "80. Favorite travel destination / City: "),
        ("favorite_cafe_bar", "81. Favorite cafe / restaurant / pub: "),
        ("native_hometown", "82. Hometown / Village: "),

        ("fav_color", "83. Favorite color: "),
        ("fav_number", "84. Favorite / Lucky number: "),
        ("fav_food", "85. Favorite food / dish: "),
        ("fav_drink", "86. Favorite drink / alcohol brand: "),
        ("fav_brand", "87. Favorite clothing/tech brand (e.g., Apple, Nike): "),
        ("fav_book", "88. Favorite book / author: "),
        ("fav_superhero", "89. Favorite superhero / fictional character: "),
        ("fav_holiday", "90. Favorite holiday (e.g., Christmas, Halloween): "),
        ("zodiac_sign", "91. Zodiac sign: "),
        ("blood_type", "92. Blood type (e.g., A+, O-): "),

        ("special_word1", "93. Frequently used phrase / Secret word 1: "),
        ("special_word2", "94. Secret word / Keyword 2: "),
        ("passphrase_base", "95. Favorite old password fragment: "),
        ("special_year1", "96. Important year 1 (e.g., graduation year): "),
        ("special_year2", "97. Important year 2 (e.g., army discharge year): "),
        ("wifi_name", "98. Home Wi-Fi network name (SSID): "),
        ("favorite_quote_word", "99. One key word from favorite motto/quote: "),
        ("extra_notes", "100. Any additional keyword/number: ")
    ]
    
    data = {}
    for key, prompt in questions:
        val = input(prompt).strip().lower()
        if val:
            data[key] = val
    return data

def apply_leetspeak(word):
    """Replaces characters with corresponding symbols/numbers"""
    leet_map = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '$', 't': '7'}
    res = word
    for char, leet in leet_map.items():
        res = res.replace(char, leet)
    return res

def generate_wordlist(data):
    base_words = set(data.values())
    generated = set()
    
    transformed_words = set()
    for w in base_words:
        transformed_words.add(w)
        transformed_words.add(w.capitalize())
        transformed_words.add(w.upper())
        transformed_words.add(apply_leetspeak(w))
        transformed_words.add(apply_leetspeak(w.capitalize()))

    generated.update(transformed_words)

    special_chars = ['', '!', '@', '#', '$', '123', '12345', '2024', '2025', '2026', '777']
    
    for w1, w2 in itertools.permutations(transformed_words, 2):
        generated.add(w1 + w2)
        for sc in special_chars:
            generated.add(w1 + sc + w2)
            generated.add(w1 + w2 + sc)

    for w in transformed_words:
        for sc in special_chars:
            if sc:
                generated.add(w + sc)
                generated.add(sc + w)

    return generated

def main():
    user_data = get_inputs()
    if not user_data:
        print("\n[-] No data was entered.")
        return

    print("\n[*] Generating wordlist...")
    wordlist = generate_wordlist(user_data)

    output_file = "custom_wordlist.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")

    print(f"[+] Successfully generated {len(wordlist)} wordlist variations.")
    print(f"[+] File saved as `{output_file}`.")

if __name__ == "__main__":
    main()