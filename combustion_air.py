#!/usr/bin/env python3
"""Combustion air supply sizing — CSA B149.1 Clause 8.
Usage: python3 combustion_air.py TOTAL_INPUT_MBH DRAFT(1/0)
Covers: Table 8.1 (tight construction, with draft control, up to 400 MBH) and
the Clause 8.4 formulas (over 400 MBH). Table 8.2 / 8.3 / 8.4 grids are not
reproduced (not publicly verifiable in full) — see combustion-air-data.json.
"""
import json, os, sys

DATA = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "combustion-air-data.json")))

def main():
    if len(sys.argv) != 3:
        print(__doc__); return
    mbh, draft = float(sys.argv[1]), sys.argv[2] == "1"
    if mbh <= 400:
        if not draft:
            print("Table 8.2 grid not reproduced in this tool. Verified points: 125 MBH -> 9 in2; 200 MBH -> 14 in2. Consult B149.1 Table 8.2.")
            return
        for row in DATA["table_8_1"]:
            if mbh <= row["max_input_mbh"]:
                print(f"Table 8.1: input rounded up to {row['max_input_mbh']} MBH")
                print(f"Required free area: {row['free_area_in2']} in2; round duct equivalent: {row['round_duct_in']} in")
                print("Duct note: sizes assume max 20 ft equivalent length; 20-50 ft -> one size up. Rectangular duct min dimension 3 in.")
                return
    else:
        if draft:
            supply = min(mbh * 1000, 1_000_000) / 7000 + max(0, mbh * 1000 - 1_000_000) / 14000
            print(f"Clause 8.4.2 supply opening: {supply:.2f} in2 (1 in2/7,000 Btu/h to 1M, then 1 in2/14,000 Btu/h), located 6-18 in above floor")
        else:
            supply = mbh * 1000 / 30000
            print(f"Clause 8.4.3 supply opening: {supply:.2f} in2 (1 in2 per 30,000 Btu/h)")
        vent = max(10.0, 0.10 * supply)
        print(f"Clause 8.4.1 ventilation opening (in addition): {vent:.2f} in2 at the highest practicable point")

if __name__ == "__main__":
    main()
