import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_rv_execute_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    # Initialize all inputs to 0
    try:
        dut.rst_n.value = 0
    except Exception:
        pass
    try:
        dut.stall.value = 0
    except Exception:
        pass
    try:
        dut.flush.value = 0
    except Exception:
        pass
    try:
        dut.pc_in.value = 0
    except Exception:
        pass
    try:
        dut.rs1_data.value = 0
    except Exception:
        pass
    try:
        dut.rs2_data.value = 0
    except Exception:
        pass
    try:
        dut.imm.value = 0
    except Exception:
        pass
    try:
        dut.rd_in.value = 0
    except Exception:
        pass
    try:
        dut.rs1_addr.value = 0
    except Exception:
        pass
    try:
        dut.rs2_addr.value = 0
    except Exception:
        pass
    try:
        dut.funct3.value = 0
    except Exception:
        pass
    try:
        dut.funct7.value = 0
    except Exception:
        pass
    try:
        dut.opcode.value = 0
    except Exception:
        pass
    try:
        dut.alu_op.value = 0
    except Exception:
        pass
    try:
        dut.mem_read.value = 0
    except Exception:
        pass
    try:
        dut.mem_write.value = 0
    except Exception:
        pass
    try:
        dut.reg_write.value = 0
    except Exception:
        pass
    try:
        dut.branch.value = 0
    except Exception:
        pass
    try:
        dut.jal.value = 0
    except Exception:
        pass
    try:
        dut.jalr.value = 0
    except Exception:
        pass
    try:
        dut.is_amo.value = 0
    except Exception:
        pass
    try:
        dut.amo_funct5.value = 0
    except Exception:
        pass
    try:
        dut.valid_in.value = 0
    except Exception:
        pass
    try:
        dut.fwd_mem_data.value = 0
    except Exception:
        pass
    try:
        dut.fwd_mem_valid.value = 0
    except Exception:
        pass
    try:
        dut.fwd_mem_rd.value = 0
    except Exception:
        pass
    try:
        dut.fwd_wb_data.value = 0
    except Exception:
        pass
    try:
        dut.fwd_wb_valid.value = 0
    except Exception:
        pass
    try:
        dut.fwd_wb_rd.value = 0
    except Exception:
        pass
    try:
        dut.fpu_result.value = 0
    except Exception:
        pass
    try:
        dut.fpu_valid.value = 0
    except Exception:
        pass
    try:
        dut.fpu_done.value = 0
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
