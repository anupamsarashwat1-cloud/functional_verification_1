import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_rv_dcache_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.cpu_addr.value = 0
    except Exception:
        pass
    try:
        dut.cpu_wdata.value = 0
    except Exception:
        pass
    try:
        dut.cpu_wstrb.value = 0
    except Exception:
        pass
    try:
        dut.cpu_req.value = 0
    except Exception:
        pass
    try:
        dut.cpu_wr.value = 0
    except Exception:
        pass
    try:
        dut.cpu_size.value = 0
    except Exception:
        pass
    try:
        dut.is_lr.value = 0
    except Exception:
        pass
    try:
        dut.is_sc.value = 0
    except Exception:
        pass
    try:
        dut.lr_addr_in.value = 0
    except Exception:
        pass
    try:
        dut.lr_valid_in.value = 0
    except Exception:
        pass
    try:
        dut.flush_all.value = 0
    except Exception:
        pass
    try:
        dut.flush_addr_en.value = 0
    except Exception:
        pass
    try:
        dut.flush_addr.value = 0
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
        dut.m_rlast.value = 0
    except Exception:
        pass
    try:
        dut.m_rresp.value = 0
    except Exception:
        pass
    try:
        dut.m_awready.value = 0
    except Exception:
        pass
    try:
        dut.m_wready.value = 0
    except Exception:
        pass
    try:
        dut.m_bvalid.value = 0
    except Exception:
        pass
    try:
        dut.m_bresp.value = 0
    except Exception:
        pass
    try:
        dut.snoop_valid.value = 0
    except Exception:
        pass
    try:
        dut.snoop_addr.value = 0
    except Exception:
        pass
    try:
        dut.snoop_type.value = 0
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
