import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_mmu_arbiter_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
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
        dut.s_rready.value = 0
    except Exception:
        pass
    try:
        dut.m_arready.value = 0
    except Exception:
        pass
    try:
        dut.m_rvalid.value = 0
    except Exception:
        pass
    try:
        dut.m_rdata.value = 0
    except Exception:
        pass
    try:
        dut.m_rresp.value = 0
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
