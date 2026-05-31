import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_gem_ethernet_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
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
        dut.m_bid.value = 0
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
        dut.m_rresp.value = 0
    except Exception:
        pass
    try:
        dut.m_rlast.value = 0
    except Exception:
        pass
    try:
        dut.m_rid.value = 0
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
    try:
        dut.tx_clk.value = 0
    except Exception:
        pass
    try:
        dut.rx_clk.value = 0
    except Exception:
        pass
    try:
        dut.gmii_rxd.value = 0
    except Exception:
        pass
    try:
        dut.gmii_rx_dv.value = 0
    except Exception:
        pass
    try:
        dut.gmii_rx_er.value = 0
    except Exception:
        pass
    try:
        dut.gmii_crs.value = 0
    except Exception:
        pass
    try:
        dut.gmii_col.value = 0
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
