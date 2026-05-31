import cocotb
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
