SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../peripherals/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../peripherals
TOPLEVEL = i2c_master
MODULE = test_i2c_master
include $(shell cocotb-config --makefiles)/Makefile.sim
