SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../backend/*.v)
VERILOG_SOURCES += $(wildcard ../../../../frontend/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../frontend -I../../../../backend
TOPLEVEL = rv_monitor_core
MODULE = test_rv_monitor_core
include $(shell cocotb-config --makefiles)/Makefile.sim
