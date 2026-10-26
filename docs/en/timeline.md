[Lire en français](../fr/timeline.md)

# Development timeline

Dates below come from the local CAD commit history and the saved revision notes. This is a curated development log, not a verbatim chat transcript. The original repository history is not imported into this public repository.

| Date | Stage | Decision and outcome |
|---|---|---|
| 24 Oct 2026 | Initial model / R1 | Four-quadrant 19-inch, 4U structure; two board trays, ATX supplies and 120 mm fans; native, STEP and 3MF outputs |
| 25 Oct 2026 | Airflow correction / R2–R3 work | Keep hexagonal weight relief but retain a 1 mm skin; front intake and rear exhaust |
| 25 Oct 2026 | Tolerance coupon | Print PETG test pieces for biscuits, screw holes and captive nuts |
| 25 Oct 2026 | Integrated front corner | Explore Q-AV-G + EAR-G integration; reduce separate assembly pieces |
| 25 Oct 2026 | Guidance / R4 | Consolidate the full model and illustrate the central guides and blade movement |
| 25 Oct 2026 | V5 | Make each whole node removable: front, tray, fan, PSU and rear panel; external cables disconnected first |
| 25 Oct 2026 | V6 | Integrate four vertical-print tunnels, including roofs and centre half-partitions |
| 25 Oct 2026 | V7 | Replace screwed splice bars with 60 mm side walls and filament-locked interleaving fingers |
| 25 Oct 2026 | Calibrated V7 | Apply measured fits; deliver ten production plates plus an optional coupon plate |
| 26 Oct 2026 | Rail R1 | Four PETG end saddles for two metal L rails; eight M6 mountings |
| 26 Oct 2026 | Rail R2 | Rear captured groove, M4 from below, captive nut above; nominal hole 30 mm from rail end |
| 26 Oct 2026 | Rail R3 | Physical test reveals misalignment; user gives 15/35/50 mm centres; extend rear support 5 mm, use 35 mm hole |

## From separate trays to complete cassettes

![Early assembled concept — historical, not the V7 production configuration](../assets/overview.png)

![R4 guidance explanation — historical](../assets/guide-r4.png)

![Early blade motion animation — historical, not a V7 verification](../assets/motion-historical.gif)

The early animation explains sliding motion. It predates the full-cassette redesign and must not be used to infer the V7 extraction sequence or clearance validation.

![V5 complete extraction](../assets/extraction-v5.png)

## From many fasteners to integrated parts

![V6 integral tunnels](../assets/enclosure-v6.png)

![V7 low walls and pinned joint](../assets/joint-v7.png)

The joint concept was inspired by the user-supplied [ALCH Modubox product reference](https://www.alch.shop/modubox-alex/p/modubox-ikea-alex-drawer-organizer) and [video at 8:31](https://youtu.be/VcB30EIcUMY?t=511). The project uses its own geometry; no commercial model files are redistributed. A Dell enclosure photograph was a conceptual reference for an empty chassis; that third-party photograph is not included here.

## Physical feedback closes the loop

![R2 mismatch before the R3 correction](../assets/rail-offset-detail.jpg)

The failed fit is retained as evidence. The first response incorrectly treated the nominal 30 mm dimension as sufficient; the subsequent physical test and measured 35 mm target prompted R3. No successful R3 print-fit result has yet been recorded.
