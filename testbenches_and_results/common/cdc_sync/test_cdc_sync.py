import cocotb
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
