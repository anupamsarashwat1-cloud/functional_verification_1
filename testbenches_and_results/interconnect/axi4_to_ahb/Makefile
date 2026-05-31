SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../interconnect/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../interconnect
TOPLEVEL = axi4_to_ahb
MODULE = test_axi4_to_ahb
include $(shell cocotb-config --makefiles)/Makefile.sim
