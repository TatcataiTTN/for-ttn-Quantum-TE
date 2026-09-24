"""List quiz questions whose correct answer is the strictly longest option (per language)."""
import re, sys
sys.path.insert(0, "build")
import build as B
mods = B.load_modules()
R = {}
for m in mods:
    nb = B.execute(m, "vi", False)
    R[m["n"]], _ = B.harvest(nb, m, "vi")
strip = lambda s: re.sub(r"<.*?>", "", s)
for m in mods:
    for i, q in enumerate(m["quiz"]):
        for lang in ("vi", "en"):
            opts = [B.fill_only(o, lang, R[m["n"]], {}, "qa") for o in q["opts"]]
            if all(len(strip(opts[0])) > len(strip(o)) for o in opts[1:]):
                print("m%02d q%d %s: correct=%r | others=%r" % (m["n"], i + 1, lang, strip(opts[0])[:60], [strip(o)[:40] for o in opts[1:]]))
