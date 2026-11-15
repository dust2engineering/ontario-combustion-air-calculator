# Ontario Combustion Air Calculator (CSA B149.1 Clause 8)

Sizes combustion and ventilation air openings for gas appliances under CSA B149.1 Clause 8 — Table 8.1 for tight construction with draft-control devices up to 400 MBH total input, and the Clause 8.4 formulas above 400 MBH. The tables this tool does not cover are named, not silently skipped.

**Live web tool:** https://dust2engineering.github.io/ontario-combustion-air-calculator/web/

## How it works

- Up to 400 MBH with draft control: Table 8.1 lookup — free area in square inches plus the round-duct equivalent (with the 20 ft / 50 ft duct-length note).
- Over 400 MBH: Clause 8.4.2 (draft control: 1 in² per 7,000 Btu/h to 1M, then 1 per 14,000) or 8.4.3 (power burners: 1 in² per 30,000 Btu/h), plus the 8.4.1 ventilation opening (10%, minimum 10 in²).
- Not covered: the Table 8.2 grid and loose-construction Tables 8.3/8.4 — full grids not publicly verifiable; two verified Table 8.2 points are in the data file.

## Data in this repository

- `combustion-air-data.json` — the complete Table 8.1, the Clause 8.4 formulas, the 8.2.6 enclosure-opening rule and the 8.5 louvre rules, from the B149.1-05 text and the BC Campus gas-fitter textbook, checked 2026-11-15.
- `combustion_air.py` — command-line calculator using the same data.

## Command line

```bash
python3 combustion_air.py 200 1
```

## Worked examples

- [furnace-water-heater-200mbh.md](examples/furnace-water-heater-200mbh.md)
- [boiler-plant-1400mbh.md](examples/boiler-plant-1400mbh.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: HVAC / mechanical. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
