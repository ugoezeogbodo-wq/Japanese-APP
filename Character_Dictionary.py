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

hira_2_dataset = [
    # G-Group (Dakuten)
    {"character": "が", "romaji": "ga", "status": 0, "due_time": None, "mnemonic": "it looks like か (ka) with dakuten marks!"},
    {"character": "ぎ", "romaji": "gi", "status": 0, "due_time": None, "mnemonic": "it looks like き (ki) with dakuten marks!"},
    {"character": "ぐ", "romaji": "gu", "status": 0, "due_time": None, "mnemonic": "it looks like く (ku) with dakuten marks!"},
    {"character": "げ", "romaji": "ge", "status": 0, "due_time": None, "mnemonic": "it looks like け (ke) with dakuten marks!"},
    {"character": "ご", "romaji": "go", "status": 0, "due_time": None, "mnemonic": "it looks like こ (ko) with dakuten marks!"},

    # Z/J-Group (Dakuten)
    {"character": "ざ", "romaji": "za", "status": 0, "due_time": None, "mnemonic": "it looks like さ (sa) with dakuten marks!"},
    {"character": "じ", "romaji": "ji", "status": 0, "due_time": None, "mnemonic": "it looks like し (shi) with dakuten marks!"},
    {"character": "ず", "romaji": "zu", "status": 0, "due_time": None, "mnemonic": "it looks like す (su) with dakuten marks!"},
    {"character": "ぜ", "romaji": "ze", "status": 0, "due_time": None, "mnemonic": "it looks like せ (se) with dakuten marks!"},
    {"character": "ぞ", "romaji": "zo", "status": 0, "due_time": None, "mnemonic": "it looks like そ (so) with dakuten marks!"},

    # D/Z-Group (Dakuten)
    {"character": "だ", "romaji": "da", "status": 0, "due_time": None, "mnemonic": "it looks like た (ta) with dakuten marks!"},
    {"character": "ぢ", "romaji": "ji", "status": 0, "due_time": None, "mnemonic": "it looks like ち (chi) with dakuten marks!"},
    {"character": "づ", "romaji": "zu", "status": 0, "due_time": None, "mnemonic": "it looks like つ (tsu) with dakuten marks!"},
    {"character": "で", "romaji": "de", "status": 0, "due_time": None, "mnemonic": "it looks like て (te) with dakuten marks!"},
    {"character": "ど", "romaji": "do", "status": 0, "due_time": None, "mnemonic": "it looks like と (to) with dakuten marks!"},

    # B-Group (Dakuten)
    {"character": "ば", "romaji": "ba", "status": 0, "due_time": None, "mnemonic": "it looks like は (ha) with dakuten marks!"},
    {"character": "び", "romaji": "bi", "status": 0, "due_time": None, "mnemonic": "it looks like ひ (hi) with dakuten marks!"},
    {"character": "ぶ", "romaji": "bu", "status": 0, "due_time": None, "mnemonic": "it looks like ふ (fu) with dakuten marks!"},
    {"character": "べ", "romaji": "be", "status": 0, "due_time": None, "mnemonic": "it looks like へ (he) with dakuten marks!"},
    {"character": "ぼ", "romaji": "bo", "status": 0, "due_time": None, "mnemonic": "it looks like ほ (ho) with dakuten marks!"},

    # P-Group (Handakuten - the small circle)
    {"character": "ぱ", "romaji": "pa", "status": 0, "due_time": None, "mnemonic": "it looks like は (ha) with a handakuten circle!"},
    {"character": "ぴ", "romaji": "pi", "status": 0, "due_time": None, "mnemonic": "it looks like ひ (hi) with a handakuten circle!"},
    {"character": "ぷ", "romaji": "pu", "status": 0, "due_time": None, "mnemonic": "it looks like ふ (fu) with a handakuten circle!"},
    {"character": "ぺ", "romaji": "pe", "status": 0, "due_time": None, "mnemonic": "it looks like へ (he) with a handakuten circle!"},
    {"character": "ぽ", "romaji": "po", "status": 0, "due_time": None, "mnemonic": "it looks like ほ (ho) with a handakuten circle!"}
]

katakana_dataset = [
    {"character": "ア", "romaji": "a", "status": 0, "due_time": None, "mnemonic": "a person with their arms stretched above their head. ✨"},
    {"character": "イ", "romaji": "i", "status": 0, "due_time": None, "mnemonic": "this as two i (parallel lines), with the second one being shorter."},
    {"character": "ウ", "romaji": "u", "status": 0, "due_time": None, "mnemonic": "a bird with its beak pointing up."},
    {"character": "エ", "romaji": "e", "status": 0, "due_time": None, "mnemonic": "a capital letter E turned on its side."},
    {"character": "オ", "romaji": "o", "status": 0, "due_time": None, "mnemonic": "a fishing order hook with a line."},

    {"character": "カ", "romaji": "ka", "status": 0, "due_time": None, "mnemonic": "a ka* (cutting tool) slicing through something."},
    {"character": "キ", "romaji": "ki", "status": 0, "due_time": None, "mnemonic": "a key with a handle."},
    {"character": "ク", "romaji": "ku", "status": 0, "due_time": None, "mnemonic": "a bird’s beak saying '*ku*ckoo'. 🐦"},
    {"character": "ケ", "romaji": "ke", "status": 0, "due_time": None, "mnemonic": "a kettle pouring tea."},
    {"character": "コ", "romaji": "ko", "status": 0, "due_time": None, "mnemonic": "two lines that have gone completely apart."},

    {"character": "サ", "romaji": "sa", "status": 0, "due_time": None, "mnemonic": "a saddle on a horse."},
    {"character": "シ", "romaji": "shi", "status": 0, "due_time": None, "mnemonic": "a shelf holding up three items."},
    {"character": "ス", "romaji": "su", "status": 0, "due_time": None, "mnemonic": "a superhero’s cape fluttering."},
    {"character": "セ", "romaji": "se", "status": 0, "due_time": None, "mnemonic": "a sensei pointing at a blackboard."},
    {"character": "ソ", "romaji": "so", "status": 0, "due_time": None, "mnemonic": "a needle and thread sewing through fabric."},

    {"character": "タ", "romaji": "ta", "status": 0, "due_time": None, "mnemonic": "a table with a high back."},
    {"character": "チ", "romaji": "chi", "status": 0, "due_time": None, "mnemonic": "a cheese wedge sliding down."},
    {"character": "ツ", "romaji": "tsu", "status": 0, "due_time": None, "mnemonic": "two needles pointing up like a tsunami wave cresting. 🌊"},
    {"character": "テ", "romaji": "te", "status": 0, "due_time": None, "mnemonic": "the cross t on top of a tennis racket."},
    {"character": "ト", "romaji": "to", "status": 0, "due_time": None, "mnemonic": "a tornado spinning downward."},

    {"character": "ナ", "romaji": "na", "status": 0, "due_time": None, "mnemonic": "a nail hammered into a piece of wood."},
    {"character": "ニ", "romaji": "ni", "status": 0, "due_time": None, "mnemonic": "two nice, parallel lines."},
    {"character": "ヌ", "romaji": "nu", "status": 0, "due_time": None, "mnemonic": "a noodle looped over."},
    {"character": "ネ", "romaji": "ne", "status": 0, "due_time": None, "mnemonic": "a net hanging down."},
    {"character": "ノ", "romaji": "no", "status": 0, "due_time": None, "mnemonic": "a simple diagonal stroke saying '*no*'."},

    {"character": "ハ", "romaji": "ha", "status": 0, "due_time": None, "mnemonic": "half a house roof."},
    {"character": "ヒ", "romaji": "hi", "status": 0, "due_time": None, "mnemonic": "a hill with a slope."},
    {"character": "フ", "romaji": "fu", "status": 0, "due_time": None, "mnemonic": "a funnel with a wide opening."},
    {"character": "ヘ", "romaji": "he", "status": 0, "due_time": None, "mnemonic": "a heavy object lifting up."},
    {"character": "ホ", "romaji": "ho", "status": 0, "due_time": None, "mnemonic": "a horse standing with reins."},

    {"character": "マ", "romaji": "ma", "status": 0, "due_time": None, "mnemonic": "a mask with two eye holes."},
    {"character": "ミ", "romaji": "mi", "status": 0, "due_time": None, "mnemonic": "three miniature lines in a row."},
    {"character": "ム", "romaji": "mu", "status": 0, "due_time": None, "mnemonic": "a cow's muzzling face. 🐮"},
    {"character": "メ", "romaji": "me", "status": 0, "due_time": None, "mnemonic": "a medical needle."},
    {"character": "モ", "romaji": "mo", "status": 0, "due_time": None, "mnemonic": "a mounting hook."},

    {"character": "ヤ", "romaji": "ya", "status": 0, "due_time": None, "mnemonic": "a yacht's sail."},
    {"character": "ユ", "romaji": "yu", "status": 0, "due_time": None, "mnemonic": "a yoyo with a string curling down."},
    {"character": "ヨ", "romaji": "yo", "status": 0, "due_time": None, "mnemonic": "three yoyo strings together."},

    {"character": "ラ", "romaji": "ra", "status": 0, "due_time": None, "mnemonic": "a rabbit’s ear turned sideways. 🐰"},
    {"character": "リ", "romaji": "ri", "status": 0, "due_time": None, "mnemonic": "two rivers flowing down."},
    {"character": "ル", "romaji": "ru", "status": 0, "due_time": None, "mnemonic": "a rustling leaf curling down."},
    {"character": "レ", "romaji": "re", "status": 0, "due_time": None, "mnemonic": "a reclining chair."},
    {"character": "ロ", "romaji": "ro", "status": 0, "due_time": None, "mnemonic": "a square room with three walls."},

    {"character": "ワ", "romaji": "wa", "status": 0, "due_time": None, "mnemonic": "a wand with a loop at the top. 🪄"},
    {"character": "ヲ", "romaji": "wo", "status": 0, "due_time": None, "mnemonic": "a fishing hook catching a worm."},
    {"character": "ン", "romaji": "n", "status": 0, "due_time": None, "mnemonic": "an n shape, bending down. 🎉"}
]

kana_2_dataset = [

    # G-Group (Dakuten)
    {"character": "ガ", "romaji": "ga", "status": 0, "due_time": None, "mnemonic": "looks like カ (ka) with dakuten marks!"},
    {"character": "ギ", "romaji": "gi", "status": 0, "due_time": None, "mnemonic": "looks like キ (ki) with dakuten marks!"},
    {"character": "グ", "romaji": "gu", "status": 0, "due_time": None, "mnemonic": "looks like ク (ku) with dakuten marks!"},
    {"character": "ゲ", "romaji": "ge", "status": 0, "due_time": None, "mnemonic": "looks like ケ (ke) with dakuten marks!"},
    {"character": "ゴ", "romaji": "go", "status": 0, "due_time": None, "mnemonic": "looks like コ (ko) with dakuten marks!"},

    # Z/J-Group (Dakuten)
    {"character": "ザ", "romaji": "za", "status": 0, "due_time": None, "mnemonic": "looks like サ (sa) with dakuten marks!"},
    {"character": "ジ", "romaji": "ji", "status": 0, "due_time": None, "mnemonic": "looks like シ (shi) with dakuten marks!"},
    {"character": "ズ", "romaji": "zu", "status": 0, "due_time": None, "mnemonic": "looks like ス (su) with dakuten marks!"},
    {"character": "ゼ", "romaji": "ze", "status": 0, "due_time": None, "mnemonic": "looks like セ (se) with dakuten marks!"},
    {"character": "ゾ", "romaji": "zo", "status": 0, "due_time": None, "mnemonic": "looks like ソ (so) with dakuten marks!"},

    # D/Z-Group (Dakuten)
    {"character": "ダ", "romaji": "da", "status": 0, "due_time": None, "mnemonic": "looks like タ (ta) with dakuten marks!"},
    {"character": "ヂ", "romaji": "ji", "status": 0, "due_time": None, "mnemonic": "looks like チ (chi) with dakuten marks!"},
    {"character": "ヅ", "romaji": "zu", "status": 0, "due_time": None, "mnemonic": "looks like ツ (tsu) with dakuten marks!"},
    {"character": "デ", "romaji": "de", "status": 0, "due_time": None, "mnemonic": "looks like テ (te) with dakuten marks!"},
    {"character": "ド", "romaji": "do", "status": 0, "due_time": None, "mnemonic": "looks like ト (to) with dakuten marks!"},

    # B-Group (Dakuten)
    {"character": "バ", "romaji": "ba", "status": 0, "due_time": None, "mnemonic": "looks like ハ (ha) with dakuten marks!"},
    {"character": "ビ", "romaji": "bi", "status": 0, "due_time": None, "mnemonic": "looks like ヒ (hi) with dakuten marks!"},
    {"character": "ブ", "romaji": "bu", "status": 0, "due_time": None, "mnemonic": "looks like フ (fu) with dakuten marks!"},
    {"character": "ベ", "romaji": "be", "status": 0, "due_time": None, "mnemonic": "looks like ヘ (he) with dakuten marks!"},
    {"character": "ボ", "romaji": "bo", "status": 0, "due_time": None, "mnemonic": "looks like ホ (ho) with dakuten marks!"},

    # P-Group (Handakuten - the small circle)
    {"character": "パ", "romaji": "pa", "status": 0, "due_time": None, "mnemonic": "looks like ハ (ha) with a handakuten circle!"},
    {"character": "ピ", "romaji": "pi", "status": 0, "due_time": None, "mnemonic": "looks like ヒ (hi) with a handakuten circle!"},
    {"character": "プ", "romaji": "pu", "status": 0, "due_time": None, "mnemonic": "looks like フ (fu) with a handakuten circle!"},
    {"character": "ペ", "romaji": "pe", "status": 0, "due_time": None, "mnemonic": "looks like ヘ (he) with a handakuten circle!"},
    {"character": "ポ", "romaji": "po", "status": 0, "due_time": None, "mnemonic": "looks like ホ (ho) with a handakuten circle!"}
]

kanji_dataset = [
    {
        "character": "一", 
        "hiragana": "いち", 
        "romaji": "ichi", 
        "meaning": "one", 
        "status_meaning": 0,
        "status_reading": 0,
        "due_time_meaning": None,
        "due_time_reading": None,
        "mnemonic_meaning": "a single horizontal line representing the number one. ✨",
        "mnemonic_reading": "an itchy (ichi) finger pointing at number one."
    },
    {
        "character": "二", 
        "hiragana": "に", 
        "romaji": "ni", 
        "meaning": "two", 
        "status_meaning": 0,
        "status_reading": 0,
        "due_time_meaning": None,
        "due_time_reading": None,
        "mnemonic_meaning": "two parallel lines for the number two.",
        "mnemonic_reading": "two knees (ni) standing together."
    },
    {
        "character": "三", 
        "hiragana": "さん", 
        "romaji": "san", 
        "meaning": "three", 
        "status_meaning": 0,
        "status_reading": 0,
        "due_time_meaning": None,
        "due_time_reading": None,
        "mnemonic_meaning": "three horizontal lines stacked together.",
        "mnemonic_reading": "Santa (san) delivering three presents."
    },
    {
        "character": "日", 
        "hiragana": "ひ", 
        "romaji": "hi", 
        "meaning": "sun / day", 
        "status_meaning": 0,
        "status_reading": 0,
        "due_time_meaning": None,
        "due_time_reading": None,
        "mnemonic_meaning": "a window frame looking out at the bright sun. ☀️",
        "mnemonic_reading": "saying 'hi' to the sun every morning."
    },
    {
        "character": "月", 
        "hiragana": "つき", 
        "romaji": "tsuki", 
        "meaning": "moon / month", 
        "status_meaning": 0,
        "status_reading": 0,
        "due_time_meaning": None,
        "due_time_reading": None,
        "mnemonic_meaning": "a crescent moon hanging in the night sky with two clouds across it.",
        "mnemonic_reading": "two key (tsuki) handles shape the moon."
    }
]