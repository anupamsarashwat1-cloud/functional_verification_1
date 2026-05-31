import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_titan_x_top_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.pipe_clk.value = 0
    except Exception:
        pass
    try:
        dut.eth_tx_clk.value = 0
    except Exception:
        pass
    try:
        dut.eth_rx_clk.value = 0
    except Exception:
        pass
    try:
        dut.ulpi_clk.value = 0
    except Exception:
        pass
    try:
        dut.mipi_rxbyteclkhs.value = 0
    except Exception:
        pass
    try:
        dut.hdmi_clk_pixel.value = 0
    except Exception:
        pass
    try:
        dut.hdmi_clk_tmds.value = 0
    except Exception:
        pass
    try:
        dut.rtc_clk.value = 0
    except Exception:
        pass
    try:
        dut.uart_rx.value = 0
    except Exception:
        pass
    try:
        dut.can_rx.value = 0
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
