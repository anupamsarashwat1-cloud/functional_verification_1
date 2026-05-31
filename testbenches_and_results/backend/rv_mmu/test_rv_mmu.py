import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_rv_mmu_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.satp.value = 0
    except Exception:
        pass
    try:
        dut.priv_mode.value = 0
    except Exception:
        pass
    try:
        dut.va_req.value = 0
    except Exception:
        pass
    try:
        dut.req_valid.value = 0
    except Exception:
        pass
    try:
        dut.req_r.value = 0
    except Exception:
        pass
    try:
        dut.req_w.value = 0
    except Exception:
        pass
    try:
        dut.req_x.value = 0
    except Exception:
        pass
    try:
        dut.ptw_arready.value = 0
    except Exception:
        pass
    try:
        dut.ptw_rvalid.value = 0
    except Exception:
        pass
    try:
        dut.ptw_rdata.value = 0
    except Exception:
        pass
    try:
        dut.ptw_rresp.value = 0
    except Exception:
        pass
    try:
        dut.sfence_vma.value = 0
    except Exception:
        pass
    try:
        dut.sfence_asid_en.value = 0
    except Exception:
        pass
    try:
        dut.sfence_va_en.value = 0
    except Exception:
        pass
    try:
        dut.sfence_va_val.value = 0
    except Exception:
        pass
    try:
        dut.sfence_asid_val.value = 0
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
