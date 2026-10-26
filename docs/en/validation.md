[Lire en français](../fr/validation.md)

# Measurements, checks and remaining tests

## User-tested printer fits

| Interface | Retained value |
|---|---:|
| Rectangular biscuit J | 0.2 mm total XY clearance |
| Central biscuit X | 0.2 mm total XY clearance |
| M3 clearance hole | 3.2 mm diameter |
| M4 clearance hole | 4.3 mm diameter |
| M3 hex nut pocket | 5.7 mm across flats |
| M4 hex nut pocket | 7.2 mm across flats |

Reported on black PETG HF without sanding or deburring. The nut-test orientation was not specified, so both orientations cannot be declared independently validated. These measurements do not validate guide clearance, biscuit depth, filament passage or joint strength.

## Digital checks

The saved reports include native recalculation, dimensions, mesh closure/winding and sampled extraction positions. V7 motion was checked at discrete positions up to 430 mm, with independent-node checks as well. These are not continuous swept-volume analyses and omit flexible cables and some real fasteners.

Calibrated Bambu projects were sliced with no skipped or off-bed objects. All use one black PETG filament. Meshes that needed repair were retriangulated from STEP and compared against CAD bounds and volumes. The V7 rear-left tunnel includes a numerical mesh-only end correction of approximately 0.005 mm; its native and STEP geometry remain unchanged.

R3 rear mesh repair stays below 0.01 mm bounds error and 0.02% volume error. Both R3 plates passed their mesh/profile checks. The physical 35 mm rail alignment remains untested.

## Next test record

| Test | Acceptance to observe | Current state |
|---|---|---|
| Rear R3 fit | Rail fully seated; M4 passes through chosen hole without forcing | Pending |
| Filament coupon | Insert and remove the actual filament over full length | Pending |
| Empty cassette | Both guides engage; no binding across the middle seam | Physical result pending |
| Loaded cassette | No joint opening or unacceptable deflection; support during extraction | Pending |
| Hot enclosure | Stable temperatures and no unacceptable PETG deformation | Pending |
| Real electronics | PSU retention, I/O, NVMe and RK1 cooler clearances checked | Pending |
| Airflow | Front intake, rear exhaust, fixed seams sealed, empty bay blanked | Pending |

Record filament, machine, nozzle, plate type, slicer profile, measured offset, photographs and whether cleanup was required. Update the current version only when an actual result is available.
