SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../memory/*.v)
VERILOG_SOURCES += $(wildcard ../../../../interconnect/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../memory -I../../../../interconnect
TOPLEVEL = ddr_ctrl_top
MODULE = test_ddr_ctrl_top
include $(shell cocotb-config --makefiles)/Makefile.sim
