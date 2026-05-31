SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += ../../../../frontend/rv_fetch.v
# For include directories (params.vh, isa_constants.vh)
COMPILE_ARGS += -I../../../../common
TOPLEVEL = rv_fetch
MODULE = test_rv_fetch
include $(shell cocotb-config --makefiles)/Makefile.sim
