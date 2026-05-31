import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_icache_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.rst_n.value = 0
    dut.cpu_addr.value = 0
    dut.cpu_req.value = 0
    dut.invalidate.value = 0
    dut.m_arready.value = 0
    dut.m_rvalid.value = 0
    dut.m_rdata.value = 0
    dut.m_rlast.value = 0
    dut.m_rresp.value = 0
    
    await Timer(25, units="ns")
    dut.rst_n.value = 1
    await RisingEdge(dut.clk)
    
    # Send CPU req
    dut.cpu_req.value = 1
    dut.cpu_addr.value = 0x1000
    await RisingEdge(dut.clk)
    dut.cpu_req.value = 0
    
    # AXI AR
    while dut.m_arvalid.value == 0:
        await RisingEdge(dut.clk)
        
    dut.m_arready.value = 1
    await RisingEdge(dut.clk)
    dut.m_arready.value = 0
    
    # AXI R (8 beats)
    for i in range(8):
        dut.m_rvalid.value = 1
        dut.m_rdata.value = 0x1111111122222222
        dut.m_rlast.value = (1 if i == 7 else 0)
        await RisingEdge(dut.clk)
        
    dut.m_rvalid.value = 0
    
    # Check hit on same address
    dut.cpu_req.value = 1
    dut.cpu_addr.value = 0x1000
    await RisingEdge(dut.clk)
    await Timer(1, units="ns")
    assert dut.cpu_valid.value == 1, "Cache should hit after fill"
    assert dut.cpu_rdata.value == 0x22222222, "Data mismatch"
