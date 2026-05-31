SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../backend/*.v)
VERILOG_SOURCES += $(wildcard ../../../../frontend/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../frontend -I../../../../backend
TOPLEVEL = rv_tlb
MODULE = test_rv_tlb
include $(shell cocotb-config --makefiles)/Makefile.sim
