import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_decode_basic(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.rst_n.value = 0
    dut.stall.value = 0
    dut.flush.value = 0
    dut.pc_in.value = 0x200
    dut.instr_in.value = 0
    dut.valid_in.value = 0
    dut.wb_rd.value = 0
    dut.wb_data.value = 0
    dut.wb_we.value = 0
    
    await Timer(25, units="ns")
    dut.rst_n.value = 1
    
    # Provide ADDI x1, x0, 5 (0x00500093)
    dut.valid_in.value = 1
    dut.instr_in.value = 0x00500093
    await RisingEdge(dut.clk)
    
    # Provide next instr, check outputs for previous
    dut.valid_in.value = 0
    await RisingEdge(dut.clk)
    
    assert dut.valid_out.value == 1, "Decoder output should be valid"
    assert dut.rd.value == 1, "Expected rd=1"
    assert dut.rs1_addr.value == 0, "Expected rs1=0"
    assert dut.imm.value == 5, "Expected imm=5"
    assert dut.reg_write.value == 1, "Expected reg_write=1 for ADDI"
    assert dut.alu_op.value == 0, "Expected ALU_ADD (0)"
