import json
import sys


in_d = json.load(open("in.json", "r"))

out_d = {"complex": []}

out_d["complex"].append(
    {
        "Re": in_d["complex"][0]["Re"] + in_d["complex"][1]["Re"],
        "Im": in_d["complex"][0]["Im"] + in_d["complex"][1]["Im"],
    }
)
out_d["complex"].append(
    {
        "Re": in_d["complex"][0]["Re"] - in_d["complex"][1]["Re"],
        "Im": in_d["complex"][0]["Im"] - in_d["complex"][1]["Im"],
    }
)
out_d["complex"].append(
    {
        "Re": in_d["complex"][0]["Re"] * in_d["complex"][1]["Re"]
        - in_d["complex"][0]["Im"] * in_d["complex"][1]["Im"],
        "Im": in_d["complex"][0]["Re"] * in_d["complex"][1]["Im"]
        + in_d["complex"][0]["Im"] * in_d["complex"][1]["Re"],
    }
)

json.dump(out_d, open("out.json", "w"), indent=4)
