import datetime as dt



hiragana_dataset = [

    # Vowels
    {"character": "あ", "romaji": "a", "status": 0, "due_time": None, "mnemonic": "an 'A' symbol with an apple hanging off it, do you see it?"},
    {"character": "い", "romaji": "i", "status": 0, "due_time": None, "mnemonic": "roman numeral II for 'I'. Count, count!!"},
    {"character": "う", "romaji": "u", "status": 0, "due_time": None, "mnemonic": "a face saying 'ooo'. すごいね (Amazing, right)!"},
    {"character": "え", "romaji": "e", "status": 0, "due_time": None, "mnemonic": "a swan with an elegant neck. きれい (Pretty)..."},
    {"character": "お", "romaji": "o", "status": 0, "due_time": None, "mnemonic": "a karate kick. Ouch!!"},

    # K-line
    {"character": "か", "romaji": "ka", "status": 0, "due_time": None, "mnemonic": "a cut with a knife. The diagonal stroke slashes through. 'Ka-chop'. Be careful with that!!"},
    {"character": "き", "romaji": "ki", "status": 0, "due_time": None, "mnemonic": "a skeleton key with two notches. The classic. Once you see it, you can't unsee it."},
    {"character": "く", "romaji": "ku", "status": 0, "due_time": None, "mnemonic": "a bird's beak opening. Tweet Tweet! 🐥"},
    {"character": "け", "romaji": "ke", "status": 0, "due_time": None, "mnemonic": "a keg of beer (cylindrical, with a tap). Cheers!"},
    {"character": "こ", "romaji": "ko", "status": 0, "due_time": None, "mnemonic": "two horizontal lines, like a small box or a koi pond surface."},

    # S-line
    {"character": "さ", "romaji": "sa", "status": 0, "due_time": None, "mnemonic": "a samurai sword with one curve below. Watch out!"},
    {"character": "し", "romaji": "shi", "status": 0, "due_time": None, "mnemonic": "a fishhook hanging straight down. Hook, line, and sinker!"},
    {"character": "す", "romaji": "su", "status": 0, "due_time": None, "mnemonic": "a loop of string or a swan loop. So smooth!"},
    {"character": "せ", "romaji": "se", "status": 0, "due_time": None, "mnemonic": "a person sitting on a bench. Relaxing time~"},
    {"character": "そ", "romaji": "so", "status": 0, "due_time": None, "mnemonic": "a zigzag pattern, like sewing thread. The shape literally looks like a needle going up and down."},

    # T-line
    {"character": "た", "romaji": "ta", "status": 0, "due_time": None, "mnemonic": "a cross or plus sign (the lowercase t gone Japanese)."},
    {"character": "ち", "romaji": "chi", "status": 0, "due_time": None, "mnemonic": "a backwards 5 with a slash. Don't mix it up with 'sa'!"},
    {"character": "つ", "romaji": "tsu", "status": 0, "due_time": None, "mnemonic": "a tsunami wave from above. Just a smooth curve. Surf's up!"},
    {"character": "て", "romaji": "te", "status": 0, "due_time": None, "mnemonic": "a teabag dangling from a string. The hook on top, the bag below."},
    {"character": "と", "romaji": "to", "status": 0, "due_time": None, "mnemonic": "a toe with a thumbtack stuck in it. The vertical line is the toe, the dot is the tack. Ouch again!"},

    # N-line
    {"character": "な", "romaji": "na", "status": 0, "due_time": None, "mnemonic": "a nun with a cross. The horizontal stroke and the curve below."},
    {"character": "に", "romaji": "ni", "status": 0, "due_time": None, "mnemonic": "a knee with two parallel lines. Double jointed!"},
    {"character": "ぬ", "romaji": "nu", "status": 0, "due_time": None, "mnemonic": "a noodle with a knot. The extra loop on the right side is the noodle twist. Slurp!"},
    {"character": "ね", "romaji": "ne", "status": 0, "due_time": None, "mnemonic": "a nest with a curl. The full loop on the right is the bird tucked in. Cozy!"},
    {"character": "の", "romaji": "no", "status": 0, "due_time": None, "mnemonic": "a no-entry sign with a slash through. Round shape with one diagonal cut. Stop right there!"},

    # H-line
    {"character": "は", "romaji": "ha", "status": 0, "due_time": None, "mnemonic": "a house with a chimney (the vertical line) and two windows."},
    {"character": "ひ", "romaji": "hi", "status": 0, "due_time": None, "mnemonic": "a nose with a curve, or a smile saying 'hee'. The curve faces left. Big grin!"},
    {"character": "ふ", "romaji": "fu", "status": 0, "due_time": None, "mnemonic": "mount Fuji with two clouds on either side. Majestic view!"},
    {"character": "へ", "romaji": "he", "status": 0, "due_time": None, "mnemonic": "the simplest character in the chart. a roof, or a flat hat. Neat and tidy!"},
    {"character": "ほ", "romaji": "ho", "status": 0, "due_time": None, "mnemonic": "a house with a chimney AND a top hat. It's は wearing an extra horizontal line. Fancy house!"},

    # M-line
    {"character": "ま", "romaji": "ma", "status": 0, "due_time": None, "mnemonic": "a mama holding a child (the vertical stroke is her body). Sweet!"},
    {"character": "み", "romaji": "mi", "status": 0, "due_time": None, "mnemonic": "a 21 (twenty-one) tilted sideways. Lucky number!"},
    {"character": "む", "romaji": "mu", "status": 0, "due_time": None, "mnemonic": "a cow chewing cud, saying 'moo'. The horns and tongue stick out. Mooo!"},
    {"character": "め", "romaji": "me", "status": 0, "due_time": None, "mnemonic": "an eye looking at you. The loop is the pupil. I see you!"},
    {"character": "も", "romaji": "mo", "status": 0, "due_time": None, "mnemonic": "a fishhook with worms wriggling on it. Three short lines. Extra bait!"},

    # Y-line
    {"character": "や", "romaji": "ya", "status": 0, "due_time": None, "mnemonic": "a yak with horns. Pointy!"},
    {"character": "ゆ", "romaji": "yu", "status": 0, "due_time": None, "mnemonic": "a fish with a U-turn. Swimming fast!"},
    {"character": "よ", "romaji": "yo", "status": 0, "due_time": None, "mnemonic": "a fishing rod with a line dangling. Ready for a catch!"},

    # R-line
    {"character": "ら", "romaji": "ra", "status": 0, "due_time": None, "mnemonic": "a rabbit looking back over its shoulder. Hop hop!"},
    {"character": "り", "romaji": "ri", "status": 0, "due_time": None, "mnemonic": "two parallel lines for a river. Smooth flow!"},
    {"character": "る", "romaji": "ru", "status": 0, "due_time": None, "mnemonic": "a loop you can roll. Has a loop at the bottom. Keep rolling!"},
    {"character": "れ", "romaji": "re", "status": 0, "due_time": None, "mnemonic": "a runner's leg in motion. No loop at the bottom. Fast feet!"},
    {"character": "ろ", "romaji": "ro", "status": 0, "due_time": None, "mnemonic": "a road that ends open (no loop). Open highway!"},

    # W-line & N
    {"character": "わ", "romaji": "wa", "status": 0, "due_time": None, "mnemonic": "a wave breaking. Similar to れ but with a small extension. Splash!"},
    {"character": "を", "romaji": "wo", "status": 0, "due_time": None, "mnemonic": "nearly identical to を except used only as a grammar particle. Special duty!"},
    {"character": "ん", "romaji": "n", "status": 0, "due_time": None, "mnemonic": "a single n sound. Looks a bit like the letter h flipped. The grand finale!"}
]