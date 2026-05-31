SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../security/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../security
TOPLEVEL = drbg
MODULE = test_drbg
include $(shell cocotb-config --makefiles)/Makefile.sim
