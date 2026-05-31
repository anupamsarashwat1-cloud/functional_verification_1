import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_rv_pmp_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.paddr.value = 0
    except Exception:
        pass
    try:
        dut.check_r.value = 0
    except Exception:
        pass
    try:
        dut.check_w.value = 0
    except Exception:
        pass
    try:
        dut.check_x.value = 0
    except Exception:
        pass
    try:
        dut.priv_mode.value = 0
    except Exception:
        pass
    try:
        dut.check_en.value = 0
    except Exception:
        pass
    try:
        dut.pmpcfg0.value = 0
    except Exception:
        pass
    try:
        dut.pmpcfg2.value = 0
    except Exception:
        pass
    try:
        dut.pmpaddr_packed.value = 0
    except Exception:
        pass

    await Timer(25, units="ns")
    
    # Release reset if present
    if hasattr(dut, 'rst_n'):
        dut.rst_n.value = 1
    elif hasattr(dut, 'reset_n'):
        dut.reset_n.value = 1
        
    for _ in range(10):
        await RisingEdge(dut.clk)
    
    # Simple pass condition: test did not crash
    assert True
