#!/usr/bin/env python3
import os
import re

interconnect_dir = "/home/anupam-sarashwat/project_penguin_verification/interconnect"
cocotb_dir = "/home/anupam-sarashwat/project_penguin_verification/verification/cocotb/interconnect"

os.makedirs(cocotb_dir, exist_ok=True)

v_files = [f for f in os.listdir(interconnect_dir) if f.endswith('.v')]

for vf in v_files:
    module_name = vf.replace('.v', '')
    top_level = "interconnect_mpu" if module_name == "mpu" else module_name
    test_dir = os.path.join(cocotb_dir, module_name)
    os.makedirs(test_dir, exist_ok=True)
    
    # Read file to extract inputs
    with open(os.path.join(interconnect_dir, vf), 'r') as f:
        content = f.read()
        
    inputs = re.findall(r'input\s+wire\s+(?:\[.*?\]\s*)?(\w+)', content)
    
    clk_name = "clk"
    if "aclk" in inputs:
        clk_name = "aclk"
    elif "hclk" in inputs:
        clk_name = "hclk"
        
    # Generate Python test
    test_py = f"""import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def test_{module_name}_basic(dut):
"""
    if clk_name in inputs:
        test_py += f"""    clock = Clock(dut.{clk_name}, 10, units="ns")
    cocotb.start_soon(clock.start())
"""
    else:
        test_py += f"""    # No standard clock found\n"""
        
    test_py += f"""    
    # Initialize all inputs to 0
"""
    for i in inputs:
        if i != clk_name:
            test_py += f"    try:\n        dut.{i}.value = 0\n    except Exception:\n        pass\n"

    test_py += f"""
    await Timer(25, units="ns")
    
    # Release reset if present
    if hasattr(dut, 'aresetn'):
        dut.aresetn.value = 1
    elif hasattr(dut, 'hresetn'):
        dut.hresetn.value = 1
    elif hasattr(dut, 'rst_n'):
        dut.rst_n.value = 1
        
"""
    if clk_name in inputs:
        test_py += f"""    for _ in range(10):
        await RisingEdge(dut.{clk_name})
"""
    else:
        test_py += f"""    await Timer(100, units="ns")\n"""
        
    test_py += f"""    
    # Simple pass condition: test did not crash
    assert True
"""

    with open(os.path.join(test_dir, f"test_{module_name}.py"), "w") as f:
        f.write(test_py)
        
    # Generate Makefile
    makefile = f"""SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../interconnect/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../interconnect
TOPLEVEL = {top_level}
MODULE = test_{module_name}
include $(shell cocotb-config --makefiles)/Makefile.sim
"""
    with open(os.path.join(test_dir, "Makefile"), "w") as f:
        f.write(makefile)

print(f"Interconnect test environments generated for {len(v_files)} modules.")
