from pathlib import Path
import sys
from collections import defaultdict

folder = Path(sys.argv[1])
sorted_dict = defaultdict(list)

for p in folder.iterdir():
    if p.suffix == "":
        sorted_dict["."].append([p.stat().st_size, str(p)])
    else:
        sorted_dict[p.suffix[1:]].append([p.stat().st_size, str(p)])

sorted_dict = dict(sorted(sorted_dict.items()))

# print(sorted_dict)

for extenstion in sorted_dict:
    print(
        extenstion,
        len(sorted_dict[extenstion]),
        sum(i[0] for i in sorted_dict[extenstion]),
    )
