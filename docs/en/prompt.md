[Lire en français](../fr/prompt.md)

# Initial design prompt — historical brief

[Download the complete original French prompt](../assets/initial-prompt-fr.txt).

The original is preserved verbatim as project evidence. This English page is an **editorial translation and condensed reading guide**, not a claim that the initial design is still current. In particular, through-holes in external panels, a short removable tray, separate roofs/partitions and the original M3/M4 tolerances were superseded.

## 0. Objective

Act as a CAD engineer using the SolidCraft MCP server. Design a printable 19-inch, 4U rack containing two Mini-ITX Turing Pi 2 boards, each on a front-extracting blade; two Cooler Master MWE Bronze 750 V3 ATX supplies at the rear; and two 120 mm fans in a central wall. Use PETG on a Bambu X1C, screws and hex nuts rather than heat-set inserts, and printed alignment biscuits between quadrants. Deliver native parametric CAD, an assembly STEP, per-part 3MFs and a verification report.

## 1–3. References, workflow and coordinates

Consult the Turing Pi board, I/O and cooling documentation, the official Mini-ITX case and SolidCraft MCP/feature documentation listed in the original. Verify purchased hardware. Start a bridged MCP session if visual feedback is needed, keep sketches small, save after each finished part and export STEP/3MF per part.

Use millimetres, X across the enclosure, Y towards the rear, and Z upwards. X=0 is the middle plane; Y=0 is the front; Z=0 is the underside. Split at X=0 and Y=210. Model the right side and mirror where appropriate. The earlier Fusion coordinate system is not retained.

## 4. Original parameter set

These values are historical; use current calibrated files for fabrication.

| Parameter | Original value |
|---|---|
| rack_face_w / rack_hole_x / u | 482.6 / 232.55 / 44.45 mm |
| chassis_h / chassis_w / chassis_d | 176.5 / 446 / 424 mm |
| half_w / split_y | 223 / 210 mm |
| floor_t / top_t / wall_t / div_t | 4 / 3 / 4 / 10 mm |
| inner_h / bay_w / rail_blk | 169.5 / 214 / 16 mm |
| ear_w / ear_t / slot_l / slot_h | 30 / 5 / 12 / 7 mm |
| tp_board / tp_pcb_t | 170 / 1.6 mm |
| standoff_h / standoff_d | 15 / 7 mm |
| tray_t / tray_w / tray_d | 3 / 197 / 195 mm |
| rail_groove / face_t | 3.4 × 3 / 4 mm |
| psu_w / psu_d / psu_h | 150 / 140 / 86 mm, to measure |
| fan / fanwall_y / psu_y0 / bay_cx | 120 / 212 / 280 / 104 mm |
| bisc_l / bisc_t / bisc_w / bisc_clear | 22 / 3 / 20 / 0.2 mm |
| hole_comp / m3_clear / m4_clear | 0.2 / 3.4 / 4.5 mm |
| m3_nut_af / m3_nut_h | 5.8 / 2.6 mm |
| m4_nut_af / m4_nut_h | 7.3 / 3.4 mm |
| hex_cell / hex_rib | 14 / 2.4 mm |

## 5–6. Layout and reference equipment

The original short tray occupied Y=6…201; the front/rear seam was Y=210; fan wall Y=212; cable space started around Y=243; PSU Y=280…420; rear wall Y=420…424. Turing Pi I/O faced forwards and mains connections backwards. The original concept expected approximately 250 mm slack in the ATX lead and top intake for the PSU. Later full-cassette and airflow decisions supersede those arrangements.

Create non-printing REF envelopes: 170 × 170 × 1.6 mm PCB, 45 mm upper component envelope, 12 mm underside NVMe envelope, 150 × 140 × 86 mm PSU and 120 × 120 × 25 mm fan. The supplied Mini-ITX hole coordinates, to verify on the real board, were (6.35,10.16), (6.35,165.10), (163.83,33.02), (163.83,165.10).

## 7–9. Original construction and joining scheme

Create four Q quadrants, two CL centre partitions, two FW fan walls, four TOP covers, two EAR rack ears, two BT trays, two BF front panels, handles and BIS/BIS-X biscuits. Original quadrants were intended to print flat. Rails were grooved into the outer blocks and centre partition, with lead-in chamfers and rear stops. The board tray included standoffs, captive M3 nuts and an underside NVMe access window.

The rear quadrant included a PSU cradle, rear opening, retaining strap slots and a fan wall with a 116 mm opening and 105 mm mounting pitch. PSU fixing holes were to be measured rather than guessed. Separate covers had overlapping side skirts and screw connections. Ears had six 12 × 7 mm rack slots at Z=6.35,38.1,66.675,111.125,139.7,171.45 mm, with X=±232.55 mm centres.

The front panel included an I/O opening, a 16 mm power-button opening, a BMC reset access to locate from the real board, ventilation, a handle and two M4 retaining screws. Its position had to allow extraction without removing rack ears.

Biscuits aligned the X=0 and Y=210 seams; the central four-way biscuit joined the quadrant crossing. Screw tabs retained seams, and nut pockets were oriented for printing. The full original contains the detailed coordinates, pocket placements and dimensions.

## 10–13. Printing, verification, delivery and open questions

The initial brief used a conservative 240 × 240 × 210 mm part envelope, minimum 2.4 mm ribs, overhangs at or below 45°, and 0.6 mm elephant-foot chamfers. Current plate checks instead use the actual target X1C limits and excluded bed area.

Report per-part bounds, overall width/height/depth, rack-slot locations, reference collisions, guide travel, underside clearance, cabling reach, screenshots, volume and PETG mass. Correct or explicitly disclose failed checks. Export native CAD, neutral assembly STEP and oriented per-part 3MF, plus a BOM. Confirm PSU holes, Turing Pi version and connectors, front/rear I/O choice and cooler height before freezing hardware interfaces.

## Changes that take precedence

- Turing Pi **2.5** and RK1 active coolers.
- Outer hex pockets retain a **1 mm skin**; front-to-rear airflow.
- Full removable cassettes; external cables disconnected before removal.
- Four vertically printed integrated enclosure tunnels.
- Low cassette walls with filament-pinned joints.
- Measured V7 holes/nut pockets and total biscuit clearances.
- Rear rail R3 locking centre **35 mm from the rail end**.

See the [timeline](timeline.md) and [validation](validation.md) for why the original brief evolved.
