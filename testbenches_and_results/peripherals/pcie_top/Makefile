SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../peripherals/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../peripherals
TOPLEVEL = pcie_top
MODULE = test_pcie_top
include $(shell cocotb-config --makefiles)/Makefile.sim
