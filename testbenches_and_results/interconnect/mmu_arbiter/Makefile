SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../interconnect/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../interconnect
TOPLEVEL = mmu_arbiter
MODULE = test_mmu_arbiter
include $(shell cocotb-config --makefiles)/Makefile.sim
