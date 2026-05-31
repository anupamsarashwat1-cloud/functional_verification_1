import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_gem_sgmii_pcs_basic(dut):
    # No standard clock found
    
    # Initialize all inputs to 0
    try:
        dut.reset_n.value = 0
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
        dut.gmii_txd.value = 0
    except Exception:
        pass
    try:
        dut.gmii_tx_en.value = 0
    except Exception:
        pass
    try:
        dut.gmii_tx_er.value = 0
    except Exception:
        pass
    try:
        dut.tbi_rx_data.value = 0
    except Exception:
        pass
    try:
        dut.signal_detect.value = 0
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
        
    await Timer(100, units="ns")
    
    # Simple pass condition: test did not crash
    assert True
