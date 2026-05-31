SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../peripherals/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../peripherals
TOPLEVEL = rtc
MODULE = test_rtc
include $(shell cocotb-config --makefiles)/Makefile.sim
