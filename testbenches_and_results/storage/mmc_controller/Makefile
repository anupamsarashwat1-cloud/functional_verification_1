SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../storage/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../storage
TOPLEVEL = mmc_controller
MODULE = test_mmc_controller
include $(shell cocotb-config --makefiles)/Makefile.sim
