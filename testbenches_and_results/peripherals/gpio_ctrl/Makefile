SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(wildcard ../../../../peripherals/*.v)
VERILOG_SOURCES += $(wildcard ../../../../common/*.v)
COMPILE_ARGS += -I../../../../common -I../../../../peripherals
TOPLEVEL = gpio_ctrl
MODULE = test_gpio_ctrl
include $(shell cocotb-config --makefiles)/Makefile.sim
