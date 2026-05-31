SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += ../../../../frontend/rv_decode.v
# For include directories (params.vh, isa_constants.vh)
COMPILE_ARGS += -I../../../../common
TOPLEVEL = rv_decode
MODULE = test_rv_decode
include $(shell cocotb-config --makefiles)/Makefile.sim
