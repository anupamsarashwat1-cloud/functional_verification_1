SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../video/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../video
TOPLEVEL = isp_pipeline
MODULE = test_isp_pipeline
include $(shell cocotb-config --makefiles)/Makefile.sim
