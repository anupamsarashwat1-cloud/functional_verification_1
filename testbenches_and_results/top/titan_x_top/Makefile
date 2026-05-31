SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../top/*.v)
VERILOG_SOURCES += $(wildcard ../../../../backend/*.v)
VERILOG_SOURCES += $(wildcard ../../../../frontend/*.v)
VERILOG_SOURCES += $(wildcard ../../../../interconnect/*.v)
VERILOG_SOURCES += $(wildcard ../../../../memory/*.v)
VERILOG_SOURCES += $(wildcard ../../../../peripherals/*.v)
VERILOG_SOURCES += $(wildcard ../../../../security/*.v)
VERILOG_SOURCES += $(wildcard ../../../../storage/*.v)
VERILOG_SOURCES += $(wildcard ../../../../video/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../top -I../../../../backend -I../../../../frontend -I../../../../interconnect -I../../../../memory -I../../../../peripherals -I../../../../security -I../../../../storage -I../../../../video
TOPLEVEL = titan_x_top
MODULE = test_titan_x_top
include $(shell cocotb-config --makefiles)/Makefile.sim
