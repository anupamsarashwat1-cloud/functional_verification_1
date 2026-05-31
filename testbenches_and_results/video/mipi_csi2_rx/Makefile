SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../video/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../video
TOPLEVEL = mipi_csi2_rx
MODULE = test_mipi_csi2_rx
include $(shell cocotb-config --makefiles)/Makefile.sim
