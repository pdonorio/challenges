POWERS = {
    "left": "sbpw",
    "right": "zdqm",
}


def alphabet_war(fight, output="let's fight again!"):
    counts = {
        key: sum(letters.count(char) * (letters.find(char) + 1) for char in fight)
        for key, letters in POWERS.items()
    }
    if counts["left"] != counts["right"]:
        output = f"{sorted(counts.items(), key=lambda x: x[1], reverse=True)[0][0]} side wins!"
    return output.capitalize()


""" cool solution

def alphabet_war(fight):
    d = {'w':4,'p':3,'b':2,'s':1,
         'm':-4,'q':-3,'d':-2,'z':-1}
    r = sum(d[c] for c in fight if c in d)

    return {r==0:"Let's fight again!",
            r>0:"Left side wins!",
            r<0:"Right side wins!"
            }[True]
"""
