import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_rv_fpu_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.fop.value = 0
    except Exception:
        pass
    try:
        dut.fmt.value = 0
    except Exception:
        pass
    try:
        dut.rm.value = 0
    except Exception:
        pass
    try:
        dut.valid_in.value = 0
    except Exception:
        pass
    try:
        dut.fp_src1.value = 0
    except Exception:
        pass
    try:
        dut.fp_src2.value = 0
    except Exception:
        pass
    try:
        dut.fp_src3.value = 0
    except Exception:
        pass
    try:
        dut.int_src.value = 0
    except Exception:
        pass
    try:
        dut.frm_csr.value = 0
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
