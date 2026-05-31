SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../interconnect/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../interconnect
TOPLEVEL = qos_controller
MODULE = test_qos_controller
include $(shell cocotb-config --makefiles)/Makefile.sim
