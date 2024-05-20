import os  
import subprocess
import json
  
all_objs = list()  

'''
C_DEPS += \\
""" + '\n'.join('    ' + os.path.join(directory, dep).replace('\\', '/') + ' \\' for dep in c_deps) + """
  
# Each subdirectory must supply rules for building sources it contributes  
""" + '\n'.join(f'{os.path.relpath(obj, directory)}: {os.path.relpath(src, directory)}\n\t@echo \'Building file: $<\'\n\t@echo \'Invoking: Standard S32DS C Compiler\'\n\t${{TC_CC}} "@{obj}.args" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"\n\t@echo \'Finished building: $<\'\n\t@echo \' \'\n\n' for src, obj in zip(c_srcs, objs)) + """  
"""  
'''
compile_template = '''
{object_dir}/%.src: {src_dir}/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: TASKING C/C++ Compiler'
	${{TC_CC}} -cs  --misrac-version=2004 -D__CPU__=tc38x "-f{relative_path}/ads_paths.opt" "-f{args}" -o "$@" "$<" 
	@echo 'Finished building: $<'
	@echo ' '
    
{object_dir}/%.o: {object_dir}/%.src
	@echo 'Building file: $<'
	@echo 'Invoking: TASKING Assembler'
	${{TC_ASM}} -Og -Os --no-warnings= --error-limit=42 -o  "$@" "$<"    
	@echo 'Finished building: $<'
	@echo ' '    
'''

def read_config():
    json_dict = dict()
    fs = open('filter.json','r+')
    data = fs.read()
    if data != '':
        json_dict = json.loads(data)       
    fs.close()
    return json_dict


def generate_makefile_mk(directory, make_relative_path, default_args):  
    make_path = os.path.join('./build', directory) #.replace('\./', '/')
    if not os.path.exists(make_path):
        os.makedirs(make_path)
    makefile_mk_name = os.path.join(make_path, 'subdir.mk')  
    # print(make_path)
    c_srcs = []  
    objs = []  
    asm_srcs = []
    c_deps = []  
      
    compile_setting_file = os.path.join(make_path, 'default.args')
    with open(compile_setting_file, 'w') as f:
        f.write(default_args)
        f.close()
    
    get_dir = list()
    # 遍历目录，查找所有的.c源文件
    # 遍历目录，查找所有的.c源文件  
    '''
    for root, dirs, files in os.walk(directory):  
        for file in files:  
            if file.endswith('.c'):  
                relative_path = os.path.relpath(os.path.join(root, file), directory)  
                c_srcs.append(relative_path)  
                obj_file = os.path.splitext(relative_path)[0] + '.o'  
                objs.append(obj_file)  
                dep_file = os.path.splitext(relative_path)[0] + '.d'  
                c_deps.append(dep_file) 
                # get_dir.append(root.replace('\\', '/'))
                all_objs.append(os.path.join(directory, obj_file).replace('\\', '/'))
    '''
    file_list = os.listdir(directory)
    for file in file_list:
        cur_path = os.path.join(directory, file)
        if os.path.isdir(cur_path):
            pass
        elif file.endswith('.c'):  
            relative_path = os.path.relpath(os.path.join(directory, file), directory)  
            c_srcs.append(relative_path)  
            obj_file = os.path.splitext(relative_path)[0] + '.o'  
            objs.append(obj_file)  
            asm_file = os.path.splitext(relative_path)[0] + '.src'  
            asm_srcs.append(asm_file)
            dep_file = os.path.splitext(relative_path)[0] + '.d'  
            c_deps.append(dep_file) 
            # get_dir.append(root.replace('\\', '/'))
            all_objs.append(os.path.join(directory, obj_file).replace('\\', '/'))
    # 生成subdir.mk文件内容  
    makefile_mk_content = """  
# Automatically-generated file. Do not edit!  
  
C_SRCS += \\
""" + '\n'.join('    ' + os.path.join(make_relative_path, directory, src).replace('\\', '/') + ' \\' for src in c_srcs) + """

COMPILED_SRCS += \\
""" + '\n'.join('    ' + os.path.join(directory, asm).replace('\\', '/') + ' \\' for asm in asm_srcs) + """

OBJS += \\
""" + '\n'.join('    ' + os.path.join(directory, obj).replace('\\', '/') + ' \\' for obj in objs) + """

C_DEPS += \\
""" + '\n'.join('    ' + os.path.join(directory, dep).replace('\\', '/') + ' \\' for dep in c_deps) + '\n'
    # compile_template_str = compile_template.format(object_dir = os.path.join(os.path.relpath( os.path.dirname(os.path.abspath(directory)), (os.path.abspath(all_root)) ), directory), src_dir = os.path.join(os.path.relpath( os.path.dirname(os.path.abspath(directory)), (os.path.abspath(all_root)) ), directory))
    # RTD/src/default.args
    # relpath = os.path.relpath( os.path.dirname(os.path.abspath(directory)), (os.path.abspath(all_root)) )
    # compile_template_str = compile_template.format(object_dir = os.path.join(os.path.relpath( os.path.dirname(os.path.abspath(directory)), (os.path.abspath(all_root)) ), directory), src_dir = os.path.join(os.path.relpath( os.path.dirname(os.path.abspath(directory)), (os.path.abspath(all_root)) ), directory))

    # compile_template_str = compile_template.format(relative_path = os.path.relpath(os.path.abspath('./'), directory).replace('\\', '/'), object_dir = directory.replace('\\', '/'), src_dir = os.path.join(make_relative_path, directory).replace('\\', '/'), args=os.path.join(directory, 'default.args'))
    compile_template_str = compile_template.format(relative_path = './', object_dir = directory.replace('\\', '/'), src_dir = os.path.join(make_relative_path, directory).replace('\\', '/'), args=os.path.join(directory, 'default.args'))

    makefile_mk_content+= compile_template_str.replace('.//', './')

    # 将内容写入subdir.mk文件  
    with open(makefile_mk_name, 'w') as makefile_mk:  
        makefile_mk.write(makefile_mk_content)  
  
skip_list = ['Debug_FLASH', 'build', '.settings', 'Project_Settings']

def foreach_dir(root_dir, relative_path, default_args, filters, inc_filters):  
    get_dir = list()
    inc_list = list()
    for root, dirs, files in os.walk(root_dir):  
        try:
            if not '__pycache__' in dirs :
                    dirs.remove('__pycache__')  
        except Exception as e:
            pass

        # if (not 'Debug_FLASH' in skip_list) and (not 'build' in root) and (not 'Project_Settings' in root):
        is_make = True
        is_have_c = False
        is_in_filters = False
        for ele in skip_list:
            if(ele in root):
                is_make = False

        # for file in files:  
        #     is_filter = False
        #     if file.endswith('.h') or True:
        #         for ele in inc_filters:                    
        #             if ele.replace('\\', '/') in root.replace('\\', '/'):
        #                 is_filter = True
        is_filter = False
        for ele in inc_filters:                    
            if ele.replace('\\', '/') in root.replace('\\', '/'):
                is_filter = True        
        if root not in inc_list and (is_filter == False):
            inc_list.append(root)

        for file in files:  
            if file.endswith('.c'):
                is_have_c = True
        for ele in filters:
            if ele.replace('\\', '/') in root.replace('\\', '/'):
                is_in_filters = True
        if (is_make) and (is_have_c) and (is_in_filters == False):
            generate_makefile_mk(root, relative_path, default_args)  
            '''
            include_mk = '-include {0}'.format(root+'.mk')
            print('include', include_mk)
            '''
            get_dir.append(root.replace('\\', '/'))
            # generate_makefile_mk(root)  
    return get_dir, inc_list
    
  
if __name__ == "__main__":  
    import argparse  
    parser = argparse.ArgumentParser(description='Generate Makefiles for each directory')  
    parser.add_argument("-r", type=str, help='The root directory to start traversal')
    parser.add_argument("-a", type=str, help='The compile default args path')    
    parser.add_argument("-m", type=str, help='The makefile template')   
    parser.add_argument("-l", type=str, help='The link parameter template')   
    
    filter_config = read_config()

    args = parser.parse_args()  

    compile_make_file_path = os.path.join(args.r, 'build', 'compile.mk')
    # include_make_opt_path = os.path.join(args.r, 'build', 'ads_paths.opt')
    build_dir = os.path.join(args.r, 'build')
    if os.path.exists(build_dir) != True:
        os.mkdir(build_dir)


    # print(compile_make_file_path)
    subprocess.run(["powershell", "cp ./config/compile.mk {0}".format(compile_make_file_path) ], capture_output=True, text=True)
    # subprocess.run(["powershell", "cp ./config/ads.opt {0}".format(include_make_opt_path) ], capture_output=True, text=True)

    args_path = os.path.abspath(args.a)
    makefile_template_path = os.path.abspath(args.m)
    inc_opt_path = os.path.join(os.path.abspath(args.r), 'build', 'ads_paths.opt')  
    # root_path = args.r
    os.chdir(args.r)
    print(os.path.abspath('./'))
    root_path = './'
    
    makefile_path = os.path.abspath('./Debug_FLASH')
    relative_path = os.path.relpath( os.path.abspath(root_path), makefile_path )  
    with open(args_path, 'r') as f:
        default_args = f.read()
        
    dirs, inc_dir_list = foreach_dir(root_path, relative_path, default_args, filter_config["filter_floders"], filter_config["include_floders"])

    inc_dir_str = ''
    for inc in inc_dir_list:
        inc_dir_str+= '''-I"../{0}" '''.format(inc)
    # print(inc_dir_str)
    with open(inc_opt_path, 'w') as fs:
        fs.write(inc_dir_str.replace("\\", "/"))
        fs.close()

    # insert_content = str()
    insert_content_list = list()
    insert_content_list+= ('-include {0}'.format(dir_sub+'/subdir.mk\n') for dir_sub in dirs)
    insert_content = ''.join(insert_content_list)
    # print(dirs, insert_content)
    # for dir_sub in dirs:
        
    search_content = "# All of the sources participating in the build are defined here"  
    with open(makefile_template_path, 'r') as f:  
        lines = f.readlines()  

    line_number = None  
    for i, line in enumerate(lines):  
        if search_content in line:  
            line_number = i  
            break  
      
    if line_number is not None:  
        lines.insert(line_number + 1, insert_content)  

        with open('./build/Makefile', 'w') as file:  
            file.writelines(lines)  
            file.close()
        print("create successful.")  
    else:  
        print("create fail")

        