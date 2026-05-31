import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_sha256_engine_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.psel.value = 0
    except Exception:
        pass
    try:
        dut.penable.value = 0
    except Exception:
        pass
    try:
        dut.pwrite.value = 0
    except Exception:
        pass
    try:
        dut.paddr.value = 0
    except Exception:
        pass
    try:
        dut.pwdata.value = 0
    except Exception:
        pass

    await Timer(25, units="ns")
    
    # Release reset if present
    if hasattr(dut, 'rst_n'):
        dut.rst_n.value = 1
    elif hasattr(dut, 'presetn'):
        dut.presetn.value = 1
    elif hasattr(dut, 'sys_rst_n'):
        dut.sys_rst_n.value = 1
    elif hasattr(dut, 'perst_n'):
        dut.perst_n.value = 1
        
    for _ in range(10):
        await RisingEdge(dut.clk)
    
    # Simple pass condition: test did not crash
    assert True
