SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../security/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../security
TOPLEVEL = envm_ctrl
MODULE = test_envm_ctrl
include $(shell cocotb-config --makefiles)/Makefile.sim
