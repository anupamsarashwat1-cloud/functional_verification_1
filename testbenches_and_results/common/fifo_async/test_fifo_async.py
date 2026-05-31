import cocotb
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
