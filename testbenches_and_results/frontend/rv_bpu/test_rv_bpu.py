import cocotb
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
