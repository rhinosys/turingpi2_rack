[Lire en français](../fr/assembly.md)

# Illustrated assembly guide — V7

## 1. Identify and prepare the parts

Lay out the four tunnels, two front floors, two rear floors, two front panels, two handles, 16 BIS and two BIS-X. Keep right and left sets separate. Remove print supports and inspect the guide grooves. Do not assemble the obsolete V5 splice bars or separate V6 roof/partition parts.

![Production plates and part labels](../assets/plates-v7.png)

**Checkpoint:** all required pieces present; reference equipment bodies excluded; guide passages clear.

## 2. Assemble one empty cassette

Place BT and FOND-AR on a flat surface. Engage the floor overlap and interleave the fingers on both side walls simultaneously. The floor must remain level at the seam. Insert two straight pieces of 1.75 mm filament, approximately 61 mm long, from above. Keep a small accessible end for removal.

![Joint and vertical filament insertion](../assets/joint-v7.png)

**Checkpoint:** no rocking, opened seam or forced pin. Test the small coupon first if the joint binds. Pins lock the joint; they are not yet load-qualified structural fasteners.

## 3. Join the fixed enclosure

Dry-fit the front and rear tunnels of each side. Align their inner and outer guide channels before fitting the biscuits. Join the left/right halves with the central alignment biscuits and retained structural fasteners. BIS/BIS-X align the seams; do not rely on them alone as proven load retention.

![Four tunnels with integrated centre guidance](../assets/enclosure-v6.png)

**Checkpoint:** both guide channels remain continuous across the front/rear seam. Try an empty cassette through the full stroke without forcing it. Seal fixed seams away from moving surfaces to maintain front-to-rear airflow.

## 4. Install the fan, PSU and board

Work on the cassette outside the rack. Fit the fan to its support, with the intended airflow towards the rear. Fit the PSU in its cradle, retaining it with straps through the provided slots without covering its intake. Fit the Turing Pi board on its standoffs; check underside NVMe clearance and cooler height before tightening.

![V7 empty cassette: board area in front, fan support in the middle, PSU cradle behind](../assets/cassette-v7.png)

**Checkpoint:** real hardware fits without touching the guides; supply intake remains open; fasteners cannot contact electronics. PSU hole positions and exact retaining hardware are not finalized by the simplified CAD envelopes.

## 5. Add front panel, handle and wiring

Fasten BF to the front floor and fit its handle. Check the I/O window against the actual Turing Pi 2.5 connectors. Route all internal wiring on the removable cassette, through the fan-support cable route and away from fan blades and guide channels. No internal node cable should remain attached to the fixed enclosure.

**Checkpoint:** front-panel retention can be released without removing the screws joining panel to tray; internal cables move with the entire node.

## 6. Fit the rack supports and test extraction

Follow the separate [rail installation](rails.md) procedure. Support the enclosure along its intended bearing areas; verify clearance above the rear M4 socket roof. Seat the cassette by engaging both guides together, then retain its front panel.

![V5 full-cassette extraction concept; V7 uses filament joints instead of splice bars](../assets/extraction-v5.png)

For removal: shut down, disconnect mains and other external cables, release front retention, then pull straight while supporting the cassette. The 430 mm CAD test position is outside the guides and **must not be left cantilevered under load**. Reverse the sequence for insertion. Thermal and load tests come after the empty-fit check, not before.
