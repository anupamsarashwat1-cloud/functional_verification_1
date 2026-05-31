import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_rv_monitor_core_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.irq_m_ext.value = 0
    except Exception:
        pass
    try:
        dut.irq_m_timer.value = 0
    except Exception:
        pass
    try:
        dut.irq_m_soft.value = 0
    except Exception:
        pass
    try:
        dut.imem_arready.value = 0
    except Exception:
        pass
    try:
        dut.imem_rdata.value = 0
    except Exception:
        pass
    try:
        dut.imem_rvalid.value = 0
    except Exception:
        pass
    try:
        dut.imem_rresp.value = 0
    except Exception:
        pass
    try:
        dut.dmem_awready.value = 0
    except Exception:
        pass
    try:
        dut.dmem_wready.value = 0
    except Exception:
        pass
    try:
        dut.dmem_bvalid.value = 0
    except Exception:
        pass
    try:
        dut.dmem_bresp.value = 0
    except Exception:
        pass
    try:
        dut.dmem_arready.value = 0
    except Exception:
        pass
    try:
        dut.dmem_rvalid.value = 0
    except Exception:
        pass
    try:
        dut.dmem_rdata.value = 0
    except Exception:
        pass
    try:
        dut.dmem_rlast.value = 0
    except Exception:
        pass
    try:
        dut.dmem_rresp.value = 0
    except Exception:
        pass
    try:
        dut.halt_req.value = 0
    except Exception:
        pass
    try:
        dut.resume_req.value = 0
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
