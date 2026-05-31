SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../memory/*.v)
VERILOG_SOURCES += $(wildcard ../../../../interconnect/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../memory -I../../../../interconnect
TOPLEVEL = l2_snoop_filter
MODULE = test_l2_snoop_filter
include $(shell cocotb-config --makefiles)/Makefile.sim
