#!/usr/bin/env python3
import os

base_dir = "/home/anupam-sarashwat/project_penguin_verification/verification/cocotb/frontend"

tests = {
    "rv_fetch": {
        "verilog_files": ["../../../../frontend/rv_fetch.v"],
        "top_level": "rv_fetch",
        "test_py": """import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_fetch_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize inputs
    dut.rst_n.value = 0
    dut.stall.value = 0
    dut.flush.value = 0
    dut.branch_taken.value = 0
    dut.branch_target.value = 0
    dut.imem_arready.value = 0
    dut.imem_rvalid.value = 0
    dut.imem_rdata.value = 0
    dut.imem_rresp.value = 0
    
    await Timer(25, units="ns")
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)
    
    # FSM goes to F_REQ (arvalid=1)
    await RisingEdge(dut.clk)
    assert dut.imem_arvalid.value == 1, "Expected fetch to request instruction"
    assert dut.imem_addr.value == 0x200, "Expected reset PC 0x200" # Based on typical RESET_PC or check value
    
    # Handshake AR
    dut.imem_arready.value = 1
    await RisingEdge(dut.clk)
    dut.imem_arready.value = 0
    
    # Provide data
    dut.imem_rvalid.value = 1
    dut.imem_rdata.value = 0x00000013 # NOP
    await RisingEdge(dut.clk)
    dut.imem_rvalid.value = 0
    
    # Assert output
    assert dut.valid_out.value == 1, "Fetch output should be valid"
    assert dut.instr_out.value == 0x00000013, "Instruction mismatch"
"""
    },
    "rv_decode": {
        "verilog_files": ["../../../../frontend/rv_decode.v"],
        "top_level": "rv_decode",
        "test_py": """import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_decode_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.rst_n.value = 0
    dut.stall.value = 0
    dut.flush.value = 0
    dut.pc_in.value = 0x200
    dut.instr_in.value = 0
    dut.valid_in.value = 0
    dut.wb_rd.value = 0
    dut.wb_data.value = 0
    dut.wb_we.value = 0
    
    await Timer(25, units="ns")
    dut.rst_n.value = 1
    
    # Provide ADDI x1, x0, 5 (0x00500093)
    dut.valid_in.value = 1
    dut.instr_in.value = 0x00500093
    await RisingEdge(dut.clk)
    
    # Provide next instr, check outputs for previous
    dut.valid_in.value = 0
    await RisingEdge(dut.clk)
    
    assert dut.valid_out.value == 1, "Decoder output should be valid"
    assert dut.rd.value == 1, "Expected rd=1"
    assert dut.rs1_addr.value == 0, "Expected rs1=0"
    assert dut.imm.value == 5, "Expected imm=5"
    assert dut.reg_write.value == 1, "Expected reg_write=1 for ADDI"
    assert dut.alu_op.value == 0, "Expected ALU_ADD (0)"
"""
    },
    "rv_bpu": {
        "verilog_files": ["../../../../frontend/rv_bpu.v"],
        "top_level": "rv_bpu",
        "test_py": """import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_bpu_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.rst_n.value = 0
    dut.fetch_pc.value = 0
    dut.fetch_valid.value = 0
    dut.ex_pc.value = 0
    dut.ex_is_branch.value = 0
    dut.ex_is_jal.value = 0
    dut.ex_taken.value = 0
    dut.ex_target.value = 0
    dut.ex_valid.value = 0
    
    await Timer(25, units="ns")
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)
    
    # Train BTB and BHT with a taken branch at PC 0x100 -> 0x200
    dut.ex_valid.value = 1
    dut.ex_is_branch.value = 1
    dut.ex_taken.value = 1
    dut.ex_pc.value = 0x100
    dut.ex_target.value = 0x200
    
    for _ in range(5):
        await RisingEdge(dut.clk)
        
    dut.ex_valid.value = 0
    
    # Fetch same PC
    dut.fetch_valid.value = 1
    dut.fetch_pc.value = 0x100
    await RisingEdge(dut.clk)
    dut.fetch_valid.value = 0
    await RisingEdge(dut.clk)
    
    assert dut.pred_taken.value == 1, "Expected branch to be predicted taken after training"
    assert dut.pred_target.value == 0x200, "BTB target mismatch"
"""
    },
    "rv_icache": {
        "verilog_files": ["../../../../frontend/rv_icache.v"],
        "top_level": "rv_icache",
        "test_py": """import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_icache_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.rst_n.value = 0
    dut.cpu_addr.value = 0
    dut.cpu_req.value = 0
    dut.invalidate.value = 0
    dut.m_arready.value = 0
    dut.m_rvalid.value = 0
    dut.m_rdata.value = 0
    dut.m_rlast.value = 0
    dut.m_rresp.value = 0
    
    await Timer(25, units="ns")
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)
    
    # Send CPU req
    dut.cpu_req.value = 1
    dut.cpu_addr.value = 0x1000
    await RisingEdge(dut.clk)
    dut.cpu_req.value = 0
    
    # AXI AR
    while dut.m_arvalid.value == 0:
        await RisingEdge(dut.clk)
        
    dut.m_arready.value = 1
    await RisingEdge(dut.clk)
    dut.m_arready.value = 0
    
    # AXI R (8 beats)
    for i in range(8):
        dut.m_rvalid.value = 1
        dut.m_rdata.value = 0x1111111122222222
        dut.m_rlast.value = (1 if i == 7 else 0)
        await RisingEdge(dut.clk)
        
    dut.m_rvalid.value = 0
    
    # Check hit on same address
    dut.cpu_req.value = 1
    dut.cpu_addr.value = 0x1000
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")
    assert dut.cpu_valid.value == 1, "Cache should hit after fill"
    assert dut.cpu_rdata.value == 0x22222222, "Data mismatch"
"""
    }
}

os.makedirs(base_dir, exist_ok=True)

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
# For include directories (params.vh, isa_constants.vh)
COMPILE_ARGS += -I../../../../common
TOPLEVEL = {config['top_level']}
MODULE = test_{test_name}
include $(shell cocotb-config --makefiles)/Makefile.sim
"""
    with open(os.path.join(test_dir, "Makefile"), "w") as f:
        f.write(makefile)

print("Frontend test environments generated.")
