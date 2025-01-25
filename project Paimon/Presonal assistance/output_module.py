import assistant_detail as ad
import speak_module as sm
import database as db


def output(o):
    print(ad.name + ": " + str(o))
    if db.speak_is_on():
        sm.speak(o)
    print()

    