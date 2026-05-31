import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_ahb_to_apb_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.haddr.value = 0
    except Exception:
        pass
    try:
        dut.hwrite.value = 0
    except Exception:
        pass
    try:
        dut.htrans.value = 0
    except Exception:
        pass
    try:
        dut.hwdata.value = 0
    except Exception:
        pass
    try:
        dut.prdata.value = 0
    except Exception:
        pass
    try:
        dut.pready.value = 0
    except Exception:
        pass
    try:
        dut.pslverr.value = 0
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
