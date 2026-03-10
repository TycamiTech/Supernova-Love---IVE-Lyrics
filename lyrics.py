import sys
import time

def cetak_lirik():
    UNGU = '\033[95m'
    RESET = '\033[0m'

    lirik = [
        ("One taste and I'm fallin' deep", 0.05, 0.5),
        ("Caught up in your energy", 0.05, 0.5),
        ("Never let me go", 0.15, 0.1),
        ("Oh, babe", 0.18, 0.2),
        ("I need that kind of love", 0.08, 0.4),
        ("A supernova glowin' the dark", 0.12, 0.6),
        ("Forever I wished upon a star", 0.11, 0.4),
        ("Then you came over", 0.08, 0.3),
        ("Occupied my heart, occupied my heart", 0.08, 1.4),
        
        ("Dee-la-dee-la, da-dee-da-dee-da", 0.12, 0.2),
        ("La-dee-la-dee-la", 0.08, 1.3),
        ("Dee-la-dee-da, la-dee-la-dee-la", 0.08, 0.9),
        ("Da-dee-da-dee-da, la-dee-la-dee-la (la-dee-la-dee-da)", 0.10, 0.2),
        ("(Oh, babe, I)", 0.10, 1.5)
    ]

    print(f"\n{UNGU}--- IVE, David Guetta - Supernova Love ---\n")
    time.sleep(1)

    for baris, kecepatan, jeda in lirik:
        for karakter in baris:
            sys.stdout.write(karakter)
            sys.stdout.flush()
            time.sleep(kecepatan)
        
        print() 
        time.sleep(jeda)

    print(f"\n--- Tycami Tech ---{RESET}")

if __name__ == "__main__":
    try:
        cetak_lirik()
    except KeyboardInterrupt:

        print("\033[0m\n\nPaused.")