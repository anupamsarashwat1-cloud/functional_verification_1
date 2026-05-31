SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../peripherals/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../peripherals
TOPLEVEL = gem_sgmii_pcs
MODULE = test_gem_sgmii_pcs
include $(shell cocotb-config --makefiles)/Makefile.sim
