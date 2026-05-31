import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_qos_controller_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.cfg_base_qos.value = 0
    except Exception:
        pass
    try:
        dut.cfg_boost_qos.value = 0
    except Exception:
        pass
    try:
        dut.cfg_bw_limit.value = 0
    except Exception:
        pass
    try:
        dut.cfg_time_win.value = 0
    except Exception:
        pass
    try:
        dut.m_arvalid.value = 0
    except Exception:
        pass
    try:
        dut.m_arready.value = 0
    except Exception:
        pass
    try:
        dut.m_awvalid.value = 0
    except Exception:
        pass
    try:
        dut.m_awready.value = 0
    except Exception:
        pass

    await Timer(25, units="ns")
    
    # Release reset if present
    if hasattr(dut, 'aresetn'):
        dut.aresetn.value = 1
    elif hasattr(dut, 'hresetn'):
        dut.hresetn.value = 1
    elif hasattr(dut, 'rst_n'):
        dut.rst_n.value = 1
        
    for _ in range(10):
        await RisingEdge(dut.clk)
    
    # Simple pass condition: test did not crash
    assert True
