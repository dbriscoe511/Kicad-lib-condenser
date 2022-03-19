

input_lib = 'test/4ms_LED.kicad_sym'
output_lib = 'test/test.kicad_sym'

with open(input_lib) as fi:
    with open(output_lib, "r+") as fo:
        with open(output_lib+'.bak', "w") as fo_bak:

            fi_lines = fi.readlines()
            fi_lines = fi_lines[1:]

            fo_lines = fo.readlines()

            fo_bak.seek(0)
            for line in fo_lines:
                fo_bak.write(line)

            fo_lines = fo_lines[:-1]

            fo.seek(0)
            lines = fo_lines + fi_lines
            for line in lines:
                fo.write(line)




