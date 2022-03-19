


def combine_libs(input_lib,output_lib, backup):
    with open(input_lib) as fi:
        with open(output_lib) as fo:
            fi_lines = fi.readlines()
            fo_lines = fo.readlines()

    if backup:
        with open(output_lib+'.bak', "w") as fo_bak:
            fo_bak.seek(0)
            for line in fo_lines:
                fo_bak.write(line)

            
    with open(output_lib, "w") as fo_w:
        fo_w.seek(0)
        lines = fo_lines[:-1] + fi_lines[1:]

        print(f"{len(lines)} total lines , {len(fo_lines)} output lib, {len(fi_lines)}, input lib")

        for line in lines:
            fo_w.write(line)

#test 
combine_libs('test/RF_Mixer_dummy.kicad_sym','test/RF_Module_dummy.kicad_sym',False)




