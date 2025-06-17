from datetime import datetime
from babel.dates import format_date
from num2words import num2words

def get_ordinal(n):
    if 10 <= n % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
    return f"{n}{suffix}"

def generate_date(lang="french"):
    # Get today's date
    today = datetime.today()

    if(lang == "french"):
        # 1. Day of the week (like 'mardi')
        day_of_week = format_date(today, "EEEE", locale="fr_FR")

        # 2. Day number in words (like 'dix-sept')
        day_number = num2words(today.day, lang='fr')

        # 3. Month name (like 'juin')
        month = format_date(today, "MMMM", locale="fr_FR")

        # 4. Year in words (like 'deux mille vingt-cinq')
        year = num2words(today.year, lang='fr')

        # Assemble full sentence
        full_sentence = f"Aujourd'hui, nous sommes le {day_of_week}, {day_number} {month}, {year}."
    
    elif(lang == "english"):
        # 1. Day of the week (like 'Tuesday')
        day_of_week = format_date(today, "EEEE", locale="en_US")

        # 2. Month name (like 'June')
        month = format_date(today, "MMMM", locale="en_US")

        # 3. Day number with ordinal suffix (like '17th')
        day_with_suffix = get_ordinal(today.day)

        # Assemble full sentence
        full_sentence = f"Today it is {day_of_week}, the {day_with_suffix} {month}, {today.year}." 

    return full_sentence

