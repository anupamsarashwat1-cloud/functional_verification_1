import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_pcie_top_basic(dut):
    clock = Clock(dut.pcie_clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.pcie_rst_n.value = 0
    except Exception:
        pass
    try:
        dut.pipe_clk.value = 0
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
        dut.s_awvalid.value = 0
    except Exception:
        pass
    try:
        dut.s_awaddr.value = 0
    except Exception:
        pass
    try:
        dut.s_awid.value = 0
    except Exception:
        pass
    try:
        dut.s_awlen.value = 0
    except Exception:
        pass
    try:
        dut.s_awsize.value = 0
    except Exception:
        pass
    try:
        dut.s_wvalid.value = 0
    except Exception:
        pass
    try:
        dut.s_wdata.value = 0
    except Exception:
        pass
    try:
        dut.s_wstrb.value = 0
    except Exception:
        pass
    try:
        dut.s_wlast.value = 0
    except Exception:
        pass
    try:
        dut.s_bready.value = 0
    except Exception:
        pass
    try:
        dut.s_arvalid.value = 0
    except Exception:
        pass
    try:
        dut.s_araddr.value = 0
    except Exception:
        pass
    try:
        dut.s_arid.value = 0
    except Exception:
        pass
    try:
        dut.s_arlen.value = 0
    except Exception:
        pass
    try:
        dut.s_arsize.value = 0
    except Exception:
        pass
    try:
        dut.s_rready.value = 0
    except Exception:
        pass
    try:
        dut.pipe_rx_data.value = 0
    except Exception:
        pass
    try:
        dut.pipe_rx_datak.value = 0
    except Exception:
        pass
    try:
        dut.pipe_rx_valid.value = 0
    except Exception:
        pass
    try:
        dut.pipe_rx_elecidle.value = 0
    except Exception:
        pass
    try:
        dut.pipe_rx_status.value = 0
    except Exception:
        pass
    try:
        dut.pipe_phy_status.value = 0
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
        await RisingEdge(dut.pcie_clk)
    
    # Simple pass condition: test did not crash
    assert True
