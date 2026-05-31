SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../video/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../video
TOPLEVEL = hdmi_ctrl
MODULE = test_hdmi_ctrl
include $(shell cocotb-config --makefiles)/Makefile.sim
