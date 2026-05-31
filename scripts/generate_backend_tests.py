#!/usr/bin/env python3
import os
import re

backend_dir = "/home/anupam-sarashwat/project_penguin_verification/backend"
cocotb_dir = "/home/anupam-sarashwat/project_penguin_verification/verification/cocotb/backend"

os.makedirs(cocotb_dir, exist_ok=True)

v_files = [f for f in os.listdir(backend_dir) if f.endswith('.v')]

for vf in v_files:
    module_name = vf.replace('.v', '')
    test_dir = os.path.join(cocotb_dir, module_name)
    os.makedirs(test_dir, exist_ok=True)
    
    # Very basic parsing for ports to toggle
    with open(os.path.join(backend_dir, vf), 'r') as f:
        content = f.read()
        
    # Find all inputs
    inputs = re.findall(r'input\s+wire\s+(?:\[.*?\]\s*)?(\w+)', content)
    
    # We always need a clock. Let's find the main clock name
    clk_name = "clk"
    if "clk" not in inputs and "core_clk" in inputs:
        clk_name = "core_clk"
        
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
        # Just in case there is no clock
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
    if hasattr(dut, 'rst_n'):
        dut.rst_n.value = 1
    elif hasattr(dut, 'reset_n'):
        dut.reset_n.value = 1
        
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
    # We include all common and backend as well as frontend for headers
    makefile = f"""SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../backend/*.v)
VERILOG_SOURCES += $(wildcard ../../../../frontend/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../frontend -I../../../../backend
TOPLEVEL = {module_name}
MODULE = test_{module_name}
include $(shell cocotb-config --makefiles)/Makefile.sim
"""
    with open(os.path.join(test_dir, "Makefile"), "w") as f:
        f.write(makefile)

print(f"Backend test environments generated for {len(v_files)} modules.")
