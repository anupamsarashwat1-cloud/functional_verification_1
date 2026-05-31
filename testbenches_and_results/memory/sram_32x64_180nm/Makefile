SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../memory/*.v)
VERILOG_SOURCES += $(wildcard ../../../../interconnect/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../memory -I../../../../interconnect
TOPLEVEL = sram_32x64_180nm
MODULE = test_sram_32x64_180nm
include $(shell cocotb-config --makefiles)/Makefile.sim
