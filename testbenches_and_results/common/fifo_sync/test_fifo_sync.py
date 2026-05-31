import cocotb
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
