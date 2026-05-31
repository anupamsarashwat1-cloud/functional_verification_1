import cocotb
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
