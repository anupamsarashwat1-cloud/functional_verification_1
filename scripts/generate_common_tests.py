#!/usr/bin/env python3
import os

base_dir = "/home/anupam-sarashwat/project_penguin_verification/verification/cocotb/common"

tests = {
    "cdc_sync": {
        "verilog_files": ["../../../../common/cdc_sync.v"],
        "top_level": "cdc_sync",
        "test_py": """import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_cdc_sync(dut):
    clock = Clock(dut.dst_clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.rst_n.value = 0
    dut.data_in.value = 0
    await Timer(25, units="ns")
    dut.rst_n.value = 1
    await RisingEdge(dut.dst_clk)
    
    # Test data propagation
    dut.data_in.value = 1
    await RisingEdge(dut.dst_clk)
    await RisingEdge(dut.dst_clk)
    await RisingEdge(dut.dst_clk)
    assert dut.data_out.value == 1, "Data did not propagate correctly"
"""
    },
    "reset_sync": {
        "verilog_files": ["../../../../common/reset_sync.v"],
        "top_level": "reset_sync",
        "test_py": """import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_reset_sync(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.async_rst_n.value = 1
    await RisingEdge(dut.clk)
    
    # Assert reset
    dut.async_rst_n.value = 0
    await Timer(5, units="ns")
    assert dut.sync_rst_n.value == 0, "Reset not asserted asynchronously"
    
    # Deassert reset
    dut.async_rst_n.value = 1
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.sync_rst_n.value == 1, "Reset not deasserted synchronously"
"""
    },
    "fifo_sync": {
        "verilog_files": ["../../../../common/fifo_sync.v"],
        "top_level": "fifo_sync",
        "test_py": """import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_fifo_sync(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.rst_n.value = 0
    dut.wr_en.value = 0
    dut.rd_en.value = 0
    dut.wr_data.value = 0
    await Timer(25, units="ns")
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)
    
    assert dut.empty.value == 1, "FIFO should be empty"
    assert dut.full.value == 0, "FIFO should not be full"
    
    # Write 1
    dut.wr_en.value = 1
    dut.wr_data.value = 0xAA
    await RisingEdge(dut.clk)
    dut.wr_en.value = 0
    await RisingEdge(dut.clk)
    
    assert dut.empty.value == 0, "FIFO should not be empty after write"
    
    # Read 1
    dut.rd_en.value = 1
    await RisingEdge(dut.clk)
    dut.rd_en.value = 0
    await Timer(1, units="ns")
    assert dut.rd_data.value == 0xAA, "Read data mismatch"
    assert dut.empty.value == 1, "FIFO should be empty after read"
"""
    },
    "fifo_async": {
        "verilog_files": ["../../../../common/fifo_async.v"],
        "top_level": "fifo_async",
        "test_py": """import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_fifo_async(dut):
    wr_clock = Clock(dut.wr_clk, 10, units="ns")
    rd_clock = Clock(dut.rd_clk, 15, units="ns")
    cocotb.start_soon(wr_clock.start())
    cocotb.start_soon(rd_clock.start())
    
    dut.wr_rst_n.value = 0
    dut.rd_rst_n.value = 0
    dut.wr_en.value = 0
    dut.rd_en.value = 0
    dut.wr_data.value = 0
    await Timer(50, units="ns")
    dut.wr_rst_n.value = 1
    dut.rd_rst_n.value = 1
    await RisingEdge(dut.wr_clk)
    
    # Write
    dut.wr_en.value = 1
    dut.wr_data.value = 0xBB
    await RisingEdge(dut.wr_clk)
    dut.wr_en.value = 0
    
    # Wait for CDC
    for _ in range(5):
        await RisingEdge(dut.rd_clk)
        
    assert dut.empty.value == 0, "FIFO should not be empty"
    
    # Read
    dut.rd_en.value = 1
    await RisingEdge(dut.rd_clk)
    dut.rd_en.value = 0
    await Timer(1, units="ns")
    assert dut.rd_data.value == 0xBB, "Read data mismatch"
"""
    }
}

for test_name, config in tests.items():
    test_dir = os.path.join(base_dir, test_name)
    os.makedirs(test_dir, exist_ok=True)
    
    # Write Python test
    with open(os.path.join(test_dir, f"test_{test_name}.py"), "w") as f:
        f.write(config["test_py"])
        
    # Write Makefile
    makefile = f"""SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += {' '.join(config['verilog_files'])}
TOPLEVEL = {config['top_level']}
MODULE = test_{test_name}
include $(shell cocotb-config --makefiles)/Makefile.sim
"""
    with open(os.path.join(test_dir, "Makefile"), "w") as f:
        f.write(makefile)

print("Test environments generated.")
