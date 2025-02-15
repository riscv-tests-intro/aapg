'''
    Module for common mappings used across registers
'''

register_mapping_int = {
    ('x', 0) : 'zero',
    ('x', 1) : 'ra',
    ('x', 2) : 'sp',
    ('x', 3) : 'gp',
    ('x', 4) : 'tp',
    ('x', 5) : 't0',
    ('x', 6) : 't1',
    ('x', 7) : 't2',
    ('x', 8) : 's0',
    ('x', 9) : 's1',
    ('x', 10) : 'a0',
    ('x', 11) : 'a1',
    ('x', 12) : 'a2',
    ('x', 13) : 'a3',
    ('x', 14) : 'a4',
    ('x', 15) : 'a5',
    ('x', 16) : 'a6',
    ('x', 17) : 'a7',
    ('x', 18) : 's2',
    ('x', 19) : 's3',
    ('x', 20) : 's4',
    ('x', 21) : 's5',
    ('x', 22) : 's6',
    ('x', 23) : 's7',
    ('x', 24) : 's8',
    ('x', 25) : 's9',
    ('x', 26) : 's10',
    ('x', 27) : 's11',
    ('x', 28) : 't3',
    ('x', 29) : 't4',
    ('x', 30) : 't5',
    ('x', 31) : 't6',
}

register_mapping_float = {
    ('f', 0): 'ft0',
    ('f', 1): 'ft1',
    ('f', 2): 'ft2',
    ('f', 3): 'ft3',
    ('f', 4): 'ft4',
    ('f', 5): 'ft5',
    ('f', 6): 'ft6',
    ('f', 7): 'ft7',
    ('f', 8): 'fs0',
    ('f', 9): 'fs1',
    ('f', 10): 'fa0',
    ('f', 11): 'fa1',
    ('f', 12): 'fa2',
    ('f', 13): 'fa3',
    ('f', 14): 'fa4',
    ('f', 15): 'fa5',
    ('f', 16): 'fa6',
    ('f', 17): 'fa7',
    ('f', 18): 'fs2',
    ('f', 19): 'fs3',
    ('f', 20): 'fs4',
    ('f', 21): 'fs5',
    ('f', 22): 'fs6',
    ('f', 23): 'fs7',
    ('f', 24): 'fs8',
    ('f', 25): 'fs9',
    ('f', 26): 'fs10',
    ('f', 27): 'fs11',
    ('f', 28): 'ft8',
    ('f', 29): 'ft9',
    ('f', 30): 'ft10',
    ('f', 31): 'ft11'
}

registers_int = [('x', i) for i in range(32)]
registers_float = [('f', i) for i in range(32)]
