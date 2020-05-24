import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

# Query for keys
query = cursor.execute("SELECT Expression FROM Dictionary")
keys = cursor.fetchall()




def get_meaning(word):
    print(keys)

    if word in keys:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
        results = cursor.fetchall()
        return results

    elif word.lower() in keys:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word.lower())
        results = cursor.fetchall()
        return results

    elif word.title() in keys:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word.title())
        results = cursor.fetchall()
        return results

    elif word.upper() in keys:
        query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word.upper())
        results = cursor.fetchall()
        return results

    elif len(get_close_matches(word,keys)) > 0:
        confirm = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, keys)[0])
        if confirm.upper() == 'Y':
            query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % get_close_matches(word, keys)[0])
            results = cursor.fetchall()
            return results

        elif confirm.upper() == 'N':
            return "The word doesn't exist. Please check it again."

        else:
            return "We didn't understand your entry"

    else:
        return "The f doesn't exist. Please check it again."
