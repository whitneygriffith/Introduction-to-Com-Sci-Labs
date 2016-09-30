def GetZodiacSign(birth_month, birth_day):
    if birth_month == 'march' and (21 <= birth_day <= 31 ):
        print("aries")
    elif birth_month == 'april' and (1 <= birth_day <= 19):
        print("aries")
    elif birth_month == 'april' and (20 <= birth_day <= 30):
        print("tauras")
    elif birth_month == 'may' and (1 <= birth_day <= 20):
        print("tauras")
    elif birth_month == 'may' and (21 <= birth_day <= 31):
        print("gemini")
    elif birth_month == 'june' and (1 <= birth_day <= 20):
        print("gemini")
    elif birth_month == 'june' and (21 <= birth_day <= 30):
        print("cancer")
    elif birth_month == 'july' and (1 <= birth_day <= 22):
        print("cancer")
    elif birth_month == 'july' and (23 <= birth_day <= 31):
        print("leo")
    elif birth_month == 'august' and (1 <= birth_day <= 22):
        print("leo")
    elif birth_month == 'august' and (23 <= birth_day <= 31):
        print("virgo")
    elif birth_month == 'september' and (1 <= birth_day <= 22):
        print("virgo")
    elif birth_month == 'september' and (23 <= birth_day <= 30):
        print("libra")
    elif birth_month == 'october' and (1 <= birth_day <= 22):
        print("libra")
    elif birth_month == 'october' and (23 <= birth_day <= 31):
        print("scorpio")
    elif birth_month == 'november' and (1 <= birth_day <= 21):
        print("scorpio")
    elif birth_month == 'november' and (22 <= birth_day <= 30):
        print("sagittarius")
    elif birth_month == 'december' and (1 <= birth_day <= 21):
        print("sagittarius")
    elif birth_month == 'december' and (22 <= birth_day <= 31):
        print("capricon")
    elif birth_month == 'january' and (1 <= birth_day <= 19):
        print("capricon")
    elif birth_month == 'january' and (20 <= birth_day <= 31):
        print("aquarius")
    elif birth_month == 'february' and (1 <= birth_day <= 18):
        print("aquarius")
    elif birth_month == 'february' and (19 <= birth_day <= 28):
        print("pisces")
    elif birth_month == 'march' and (1 <= birth_day <= 20):
        print("pisces")

        
GetZodiacSign('march', 6)
GetZodiacSign("march", 28)    
GetZodiacSign("march", 15)
GetZodiacSign("july", 21)
GetZodiacSign("february", 14)
