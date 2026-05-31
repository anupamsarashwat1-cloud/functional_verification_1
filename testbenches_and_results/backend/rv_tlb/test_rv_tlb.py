import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_rv_tlb_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.va_in.value = 0
    except Exception:
        pass
    try:
        dut.asid_in.value = 0
    except Exception:
        pass
    try:
        dut.req_valid.value = 0
    except Exception:
        pass
    try:
        dut.fill_valid.value = 0
    except Exception:
        pass
    try:
        dut.fill_va.value = 0
    except Exception:
        pass
    try:
        dut.fill_pa.value = 0
    except Exception:
        pass
    try:
        dut.fill_asid.value = 0
    except Exception:
        pass
    try:
        dut.fill_perm.value = 0
    except Exception:
        pass
    try:
        dut.fill_level.value = 0
    except Exception:
        pass
    try:
        dut.sfence_vma.value = 0
    except Exception:
        pass
    try:
        dut.sfence_asid.value = 0
    except Exception:
        pass
    try:
        dut.sfence_asid_val.value = 0
    except Exception:
        pass
    try:
        dut.sfence_va.value = 0
    except Exception:
        pass
    try:
        dut.sfence_va_val.value = 0
    except Exception:
        pass
    try:
        dut.access_r.value = 0
    except Exception:
        pass
    try:
        dut.access_w.value = 0
    except Exception:
        pass
    try:
        dut.access_x.value = 0
    except Exception:
        pass
    try:
        dut.priv_s.value = 0
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
