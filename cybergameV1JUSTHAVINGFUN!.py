xp = 0

name = input("Hey! Welcome to our cybersecurity game! What's your name, fella? : ")
print("Nice to meet you", name)

choice = input(
    "What would you want to do? new game / load the game / quit : "
).lower()

if choice == "new game":

    print("Welcome to Cybersecurity")

    level = input(
        "What level do you want? level 1 / level 2 / level 3 / level 4 : "
    ).lower()

    # =========================
    # LEVEL 1
    # =========================

    if level == "level 1":

        print("Well well well... it is Level 1.")

        puzzle = input("""
01: alex  — 192.168.1.14 — 08:42
02: mike  — 192.168.1.19 — 08:43
03: alex  — 10.0.0.7     — 08:43
04: sarah — 192.168.1.22 — 08:44
05: alex  — 10.0.0.7     — 08:44

OBJECTIVE:
Find the suspicious login attempt.
Choose one: 1 to 5
> """)

        suspect_name = input("What's the suspicious user's name? : ")
        address = input("What's the suspicious user's address? : ")

        if puzzle == "5" and suspect_name == "alex" and address == "10.0.0.7":

            xp += 100

            print("\nACCESS GRANTED")
            print("Mission completed!")
            print("XP:", xp)

        else:

            print("\nACCESS DENIED")

        # =========================
        # LEVEL 2 UNLOCK
        # =========================

        if xp < 100:

            print("You have not reached Level 2 yet.")

        else:

            print("\nWelcome to Level 2!")

            # =========================
            # LEVEL 2
            # =========================

            print("""
╔══════════════════════╗
      LEVEL 2
   SECURE TERMINAL
╚══════════════════════╝

SECURITY SYSTEM:
3-digit access code required.
""")

            print("""
CLUE 1: The first digit is 6.
CLUE 2: The second digit is 8.
CLUE 3: The third digit is 3.

ENTER CODE:
""")

            code = input("> ")

            if code == "683":

                xp += 200

                print("\nACCESS GRANTED")
                print("Mission completed!")
                print("XP:", xp)

            else:

                print("\nACCESS DENIED")

            # =========================
            # LEVEL 3 UNLOCK
            # =========================

            if xp < 300:

                print("You have not reached Level 3 yet.")

            else:

                print("\nWelcome to Level 3!")

                attempts = 3

                print("""
╔══════════════════════╗
      LEVEL 3
     SYSTEM BREACH
╚══════════════════════╝

SECURITY ALERT:
Unauthorized access detected.

You have 3 attempts to identify the correct access code.

CLUES:

1. The first digit is 7.
2. The second digit is 3.
3. The third digit is 9.
4. The fourth digit is 2.
""")

                while attempts > 0:

                    print("Attempts remaining:", attempts)

                    code = input("ENTER ACCESS CODE: ")

                    if code == "7392":

                        xp += 300

                        print("\nACCESS GRANTED")
                        print("Mission completed!")
                        print("XP:", xp)

                        break

                    else:

                        attempts -= 1
                        print("ACCESS DENIED")

                # =========================
                # LEVEL 4 UNLOCK
                # =========================

                if xp < 600:

                    print("Level 3 failed. Level 4 is locked.")

                else:

                    print("\nWelcome to Level 4!")
                    print("THE FINAL ROUND!")

                    # =========================
                    # LEVEL 4
                    # =========================

                    print("""
╔════════════════════════════════╗
        LEVEL 4 — THE BREACH
╚════════════════════════════════╝

🚨 CRITICAL ALERT

Someone has accessed the central server.

Three suspects were active during the breach:

01 — ALEX
IP: 10.0.0.7
TIME: 02:13

02 — MIKE
IP: 192.168.1.19
TIME: 14:32

03 — SARAH
IP: 172.16.0.4
TIME: 02:17

INTELLIGENCE REPORT:

• The attacker used an internal IP.
• The breach occurred between 02:00 and 03:00.
• The attacker attempted access twice.
• One suspect's IP appeared in both attempts.
""")

                    suspect = input("IDENTIFY ATTACKER: ")
                    ip = input("IDENTIFY IP: ")
                    codes = input("FINAL AUTHORIZATION CODE: ")

                    if suspect.lower() == "alex" and ip == "10.0.0.7" and codes == "7392":

                        xp += 500

                        print("\n🔥 BREACH CONTAINED 🔥")
                        print("MISSION COMPLETE!")
                        print("FINAL XP:", xp)

                    else:

                        print("\nMISSION FAILED")

    # =========================
    # LOCKED LEVELS
    # =========================

    elif level == "level 2":

        print("Level 2 is currently locked.")

    elif level == "level 3":

        print("Level 3 is currently locked.")

    elif level == "level 4":

        print("Level 4 is currently locked.")

    else:

        print("Invalid level.")


elif choice == "load the game":

    print("The save system isn't built yet.")


elif choice == "quit":

    print("Goodbye!")


else:

    print("Invalid choice.")