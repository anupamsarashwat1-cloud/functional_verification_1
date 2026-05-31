SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += ../../../../frontend/rv_icache.v
# For include directories (params.vh, isa_constants.vh)
COMPILE_ARGS += -I../../../../common
TOPLEVEL = rv_icache
MODULE = test_rv_icache
include $(shell cocotb-config --makefiles)/Makefile.sim
