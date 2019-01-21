template_config = '''
# Sample config.ini file to generate a random program
# using aapg (Automated Assembly Program Generator)

# Each section commands a behaviour of aapg
# and inline comments in each section will explain the
# usage

# ---------------------------------------------------------------------------------
# General directives to aapg
# Options:
#       total_instructions: Approximate number of instructions to be generated
#                           by aapg. Actual may vary.
#       regs_not_use:       Comma separated list of RISC-V registers to not use for
#                           reading/writing in the random generated instructions
# ---------------------------------------------------------------------------------
[general]
total_instructions = 1000
regs_not_use = x1,x2
user_trap_handler = false
code_start_address = 0x80000000
default_program_exit = true

# ---------------------------------------------------------------------------------
# Distribution of instructions according to ISA extensions
# Specify the relative frequency of each set 
# E.g. : A relative frequency of 1 each means each instruction will be 
# generated equal number of times in the total instructions. Specify 0 to disable.
# ---------------------------------------------------------------------------------
[isa-instruction-distribution]
rel_sys = 0
rel_sys.csr = 0
rel_rv32i.ctrl = 0
rel_rv32i.compute = 1
rel_rv32i.data = 0
rel_rv32i.fence = 0
rel_rv64i.compute = 0
rel_rv64i.data = 0
rel_rv32m = 0
rel_rv64m = 0
rel_rv32a = 0
rel_rv64a = 0
rel_rv32f = 0
rel_rv64f = 0
rel_rv32d = 0
rel_rv64d = 0

# Compressed instructions

rel_rvc.ctrl = 0
rel_rvc.compute = 0
rel_rvc.sp = 0
rel_rvc.data = 0
rel_rvc.fdata = 0

rel_rv32c.compute = 0
rel_rv32c.ctrl = 0
rel_rv32c.fdata = 0

rel_rv64c.compute = 0
rel_rv64c.data = 0

[branch-control]
backward-probability = 0.5

# ---------------------------------------------------------------------------------
# Recursion options
# Options:
#       recursion_enable:   Generate the template for recursion or not
#       recursion_depth:    Number of times the recursive function is called
# ---------------------------------------------------------------------------------
[recursion-options]
recursion-enable = false
recursion-depth = 10
recursion-calls = 5

# ---------------------------------------------------------------------------------
# Data access sections
# Specify which regions of memory will be accessed by the random program
# Options:
#       enable:         Force all memory accesses instructions to only load/store
#                       to the specified list of address sections
#                       
# Section Template: Specify legal access zones using the following template
#       section_name =  section_low,section_high (HEX)     
# ---------------------------------------------------------------------------------
[access-sections]
section1 = 0x90000000,0x90001000,rw
section2 = 0x90001000,0x90002000,r

# ---------------------------------------------------------------------------------
# User template sections
# Allows users to specify call to a custom function with number of times to call
# User should ensure that function does not modify 
#                       
# Section Template: Specify user template function calls with the number of times
#       function_name = number_of_times
# ---------------------------------------------------------------------------------
[user-functions]
_test = 0

# ---------------------------------------------------------------------------------
# Instruction Cache and Data-Cache Thrashing
# ---------------------------------------------------------------------------------
[i-cache]
num_calls = 0
num_bytes_per_block = 16
num_blocks = 8
num_cycles = 10

[d-cache]
num_calls = 0
num_bytes_per_block = 16
num_blocks = 8
num_cycles = 10

# ---------------------------------------------------------------------------------
# Exception generation
# ---------------------------------------------------------------------------------
[exception-generation]
ecause00 = 0
ecause01 = 0
ecause02 = 0
ecause03 = 0
ecause04 = 0
ecause05 = 0
ecause06 = 0
ecause07 = 0
ecause08 = 0
ecause09 = 0
ecause10 = 0
ecause11 = 0
ecause12 = 0
ecause13 = 0
ecause14 = 0

# ---------------------------------------------------------------------------------
# Data Hazards
# ---------------------------------------------------------------------------------
[data-hazards]
raw_prob = 0.5
war_prob = 0.5
waw_prob = 0.5
num_regs_lookbehind = 3
'''
