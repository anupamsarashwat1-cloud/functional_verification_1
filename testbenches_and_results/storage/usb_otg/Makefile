SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../storage/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../storage
TOPLEVEL = usb_otg
MODULE = test_usb_otg
include $(shell cocotb-config --makefiles)/Makefile.sim
