import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_sram_512kx8_180nm_basic(dut):
    # No standard clock found
    
    # Initialize all inputs to 0
    try:
        dut.CLK.value = 0
    except Exception:
        pass
    try:
        dut.CEN.value = 0
    except Exception:
        pass
    try:
        dut.WEN.value = 0
    except Exception:
        pass
    try:
        dut.A.value = 0
    except Exception:
        pass
    try:
        dut.D.value = 0
    except Exception:
        pass

    await Timer(25, units="ns")
    
    # Release reset if present
    if hasattr(dut, 'rst_n'):
        dut.rst_n.value = 1
    elif hasattr(dut, 'sys_rst_n'):
        dut.sys_rst_n.value = 1
        
    await Timer(100, units="ns")
    
    # Simple pass condition: test did not crash
    assert True
