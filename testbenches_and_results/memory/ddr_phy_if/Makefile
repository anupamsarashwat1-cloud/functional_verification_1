SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../memory/*.v)
VERILOG_SOURCES += $(wildcard ../../../../interconnect/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../memory -I../../../../interconnect
TOPLEVEL = ddr_phy_if
MODULE = test_ddr_phy_if
include $(shell cocotb-config --makefiles)/Makefile.sim
