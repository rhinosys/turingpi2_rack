[Lire en français](../fr/index.md)

# A printable enclosure with two complete removable blades

This project develops a 19-inch, 4U enclosure for two Turing Pi 2.5 boards and two ATX power supplies. Each board is intended to carry RK1 modules with their heatsinks and fans. The electronics shown in CAD are simplified envelopes; final component clearances still require measurement.

The fixed enclosure provides structure, guidance and an air path. Each removable cassette carries its front panel, board tray, fan, power supply and rear panel. **Shut down and disconnect external cables before extraction.** There is no blind-mate backplane or hot-swap mechanism.

![V7 cassette with low side walls](../assets/cassette-v7.png)

## Start here

1. Read the [architecture and parts](architecture.md).
2. Use the [calibrated files](files.md), then follow the [printing guide](printing.md).
3. Build one node using the [illustrated assembly guide](assembly.md).
4. Fit the [R3 rail supports](rails.md).
5. Read [test results and remaining work](validation.md) before treating the prototype as finished hardware.

## Current status

| Item | Status |
|---|---|
| Rack V7 | Native CAD, STEP, geometry exports and sliced Bambu projects available |
| Measured fits | J0.2, X0.2, M3/M4 holes and nut pockets reported to fit without cleanup |
| Rear rail R3 | Hole moved from 30 to 35 mm; geometry and slicing checked; physical fit pending |
| Complete loaded rack | Mechanical strength, hot PETG creep and thermal performance not qualified |

CAD colours identify components. Production files use **one black PETG filament**. Version history is available in the [timeline](timeline.md); the [initial prompt](prompt.md) is historical, not the current build specification.
