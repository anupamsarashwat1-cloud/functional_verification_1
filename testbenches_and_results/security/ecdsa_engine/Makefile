SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../security/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../security
TOPLEVEL = ecdsa_engine
MODULE = test_ecdsa_engine
include $(shell cocotb-config --makefiles)/Makefile.sim
