# Project Penguin TITAN-X Functional Verification

Welcome to the `functional_verification_1` repository! This repository acts as the central hub for the documentation, automated test frameworks, simulation logs, and final sign-off reports for the **TITAN-X SoC (Project Penguin)** RTL design.

## 🎯 Overview
The goal of this verification effort was to take a complex System-on-Chip (SoC) featuring 4x RV64GC cores, 1x RV64IMAC monitor core, an AXI4 crossbar, L2 caches, DDR4 memory subsystems, cryptographic engines, high/low-speed peripherals, and a video pipeline, and systematically verify that it elaborates cleanly and passes foundational sanity checks under Icarus Verilog (`iverilog`).

## 📋 Verification Strategy & Plan
To achieve full SoC verification without overwhelming the simulation environment, we employed a **bottom-up, 11-Gate sign-off strategy**. 

Instead of compiling the top-level SoC right away, we built Python-based automated test generators (`verification/scripts/generate_*_tests.py`) that crawled the RTL directories, extracted module port definitions, and generated standalone Cocotb/Python testbenches for **every single module**.

You can review our original verification plan here: [`plan_and_strategy.md`](./plan_and_strategy.md)

## 🛠 Methods & Steps (The 11 Gates)
We incrementally integrated and verified the SoC across 11 distinct gates:
- **Gate 1 (Common & Base IP):** FIFOs, Synchronizers.
- **Gate 2 (CPU Frontend):** Fetch, Decode, BPU, I-Cache.
- **Gate 3 (CPU Backend & RV64 Core):** Execution units, FPU, MMU, PMP.
- **Gate 4 (Interconnect):** AXI4 Crossbar, APB Bridges, QoS Controllers.
- **Gate 5 (Memory Subsystem):** L2 Cache, SRAM arrays, DDR4 Controller.
- **Gate 6 (Security):** Secure Boot, ECDSA Engine, DRBG, eNVM Controller.
- **Gate 7 (Crypto Peripherals):** AES, SHA256, TRNG.
- **Gate 8 (Communication Peripherals):** UART, I2C, SPI, CAN, Ethernet, PCIe, GPIO, RTC, Watchdog.
- **Gate 9 (Storage):** USB OTG, MMC, QSPI.
- **Gate 10 (Video):** MIPI CSI-2 RX, ISP Pipeline, VDMA, HDMI Controller.
- **Gate 11 (Full SoC):** `titan_x_top.v` full integration test.

Detailed descriptions of every step and methodology are recorded in our execution report: [`methods_steps_changes_results.md`](./methods_steps_changes_results.md)
The checklist of all targets hit is available in: [`verification_tasks.md`](./verification_tasks.md)

## ⚙️ Scripts, Testbenches, and Framework
We heavily utilized `Cocotb` alongside Python automation. 
- **`scripts/`**: Contains Python scripts (e.g., `generate_backend_tests.py`, `generate_interconnect_tests.py`) that parse Verilog files using Regular Expressions to identify clock/reset inputs and automatically spawn test structures.
- **`testbenches_and_results/`**: Contains the generated `test_*.py` files, `Makefile` configurations linking `iverilog`, and the final Cocotb `results.xml` output files proving success.

## 🔧 RTL Changes & Bug Fixes
During the verification effort, we discovered a few structural and syntactical incompatibilities in the original design that prevented simulation in Icarus Verilog. The following design changes were implemented (and pushed to the main `Project_penguin2` repository):

1. **`backend/rv_fpu.v`**: Removed `$shortrealtobits` and `$bitstoshortreal` SystemVerilog floating-point casting calls, which Icarus Verilog does not support.
2. **`video/mipi_csi2_rx.v`**: Flattened unpacked arrays (`[7:0] rxdatahs [0:LANES-1]`) into single packed arrays for structural compatibility.
3. **`top/titan_x_top.v`**: Replaced the unsupported `{default: ...}` array struct syntax mapping with standard packed assignments on the MIPI CSI-2 receiver instantiation.

## 📊 Logs & Results
Every single module (totaling 43 IP blocks + Top Level) was successfully compiled and simulated. Basic reset vectors and clock toggling sanity tests PASSED across the board.

- **`logs/`**: Contains the raw stdout logs from our static linters (`lint_report.html`, `lint.log`) and full compilation traces (`compile.log`).
- **`testbenches_and_results/.../results.xml`**: Machine-readable JUnit XML outputs from Cocotb verifying individual module success.

***

**Status**: ✅ *Sign-off Complete. TITAN-X RTL is structurally sound and ready for advanced functional test targeting.*
