SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../interconnect/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../interconnect
TOPLEVEL = axi4_crossbar
MODULE = test_axi4_crossbar
include $(shell cocotb-config --makefiles)/Makefile.sim
