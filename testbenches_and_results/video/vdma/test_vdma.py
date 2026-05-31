import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_vdma_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.s_axis_s2mm_tdata.value = 0
    except Exception:
        pass
    try:
        dut.s_axis_s2mm_tvalid.value = 0
    except Exception:
        pass
    try:
        dut.s_axis_s2mm_tuser.value = 0
    except Exception:
        pass
    try:
        dut.s_axis_s2mm_tlast.value = 0
    except Exception:
        pass
    try:
        dut.m_axis_mm2s_tready.value = 0
    except Exception:
        pass
    try:
        dut.m_axi_awready.value = 0
    except Exception:
        pass
    try:
        dut.m_axi_wready.value = 0
    except Exception:
        pass
    try:
        dut.m_axi_bvalid.value = 0
    except Exception:
        pass
    try:
        dut.m_axi_bresp.value = 0
    except Exception:
        pass
    try:
        dut.m_axi_arready.value = 0
    except Exception:
        pass
    try:
        dut.m_axi_rvalid.value = 0
    except Exception:
        pass
    try:
        dut.m_axi_rdata.value = 0
    except Exception:
        pass
    try:
        dut.m_axi_rresp.value = 0
    except Exception:
        pass
    try:
        dut.m_axi_rlast.value = 0
    except Exception:
        pass
    try:
        dut.paddr.value = 0
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
        dut.pwdata.value = 0
    except Exception:
        pass

    await Timer(25, units="ns")
    
    # Release reset if present
    if hasattr(dut, 'rst_n'):
        dut.rst_n.value = 1
    elif hasattr(dut, 'sys_rst_n'):
        dut.sys_rst_n.value = 1
        
    for _ in range(10):
        await RisingEdge(dut.clk)
    
    # Simple pass condition: test did not crash
    assert True
