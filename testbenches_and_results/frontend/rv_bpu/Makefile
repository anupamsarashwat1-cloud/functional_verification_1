SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += ../../../../frontend/rv_bpu.v
# For include directories (params.vh, isa_constants.vh)
COMPILE_ARGS += -I../../../../common
TOPLEVEL = rv_bpu
MODULE = test_rv_bpu
include $(shell cocotb-config --makefiles)/Makefile.sim
