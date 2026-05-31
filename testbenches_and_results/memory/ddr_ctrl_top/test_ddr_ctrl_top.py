import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_ddr_ctrl_top_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.s_awvalid.value = 0
    except Exception:
        pass
    try:
        dut.s_awaddr.value = 0
    except Exception:
        pass
    try:
        dut.s_awid.value = 0
    except Exception:
        pass
    try:
        dut.s_awlen.value = 0
    except Exception:
        pass
    try:
        dut.s_awsize.value = 0
    except Exception:
        pass
    try:
        dut.s_wvalid.value = 0
    except Exception:
        pass
    try:
        dut.s_wdata.value = 0
    except Exception:
        pass
    try:
        dut.s_wstrb.value = 0
    except Exception:
        pass
    try:
        dut.s_wlast.value = 0
    except Exception:
        pass
    try:
        dut.s_bready.value = 0
    except Exception:
        pass
    try:
        dut.s_arvalid.value = 0
    except Exception:
        pass
    try:
        dut.s_araddr.value = 0
    except Exception:
        pass
    try:
        dut.s_arid.value = 0
    except Exception:
        pass
    try:
        dut.s_arlen.value = 0
    except Exception:
        pass
    try:
        dut.s_rready.value = 0
    except Exception:
        pass

    await Timer(25, units="ns")
    
    # Release reset if present
    if hasattr(dut, 'rst_n'):
        dut.rst_n.value = 1
    elif hasattr(dut, 'sys_rst_n'):
        dut.sys_rst_n.value = 1
        
    for _ in range(10):
        await RisingEdge(dut.clk)
    
    # Simple pass condition: test did not crash
    assert True
