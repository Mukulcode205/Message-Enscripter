d1 = {"a":"!", "b":"@", "c":"#", "d":"$", "e":"^", "f":"&", "g":"*", "h":")",
"i":"(", "j":"-", "k":"_", "l":"+", "m":"=", "n":"{", "o":"}", "p":"[",
"q":"]", "r":":", "s":";", "t":"'", "u":"<", "v":",", "w":">", "x":".",
"y":"?", "z":"/", " ":"`"}
d2= {"!":"a", "@":"b", "#":"c", "$":"d", "^":"e", "&":"f", "*":"g", "(":"h",
")":"i", "-":"j", "_":"k", "+":"l", "=":"m", "{":"n", "}":"o", "[":"p",
"]":"q", ":":"r", ";":"s", "'":"t", "<":"u", ",":"v", ">":"w", ".":"x",
"?":"y", "/":"z", "`":" "}
try:
    user_ip_1 = int(input("Press 1 to enscript\npress 2 to descript\n>>>"))
    if user_ip_1 == 1:
        user_ip_2 = input("Enter the message to Enscript\n>>>")
        for x in user_ip_2:
            print(d1[x], end="")
    elif user_ip_1 == 2:
        user_ip_3 = input("Enterthe message to Descript\n>>>")
        for y in user_ip_3:
            print(d2[y], end="")
except Exception as e:
    print("Warning: Unknown fatal error '404'")
