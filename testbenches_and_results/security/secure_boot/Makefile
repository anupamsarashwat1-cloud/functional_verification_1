SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../security/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../security
TOPLEVEL = secure_boot
MODULE = test_secure_boot
include $(shell cocotb-config --makefiles)/Makefile.sim
