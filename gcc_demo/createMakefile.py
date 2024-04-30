import os  
import subprocess
 
  
all_objs = list()  

'''
C_DEPS += \\
""" + '\n'.join('    ' + os.path.join(directory, dep).replace('\\', '/') + ' \\' for dep in c_deps) + """
  
# Each subdirectory must supply rules for building sources it contributes  
""" + '\n'.join(f'{os.path.relpath(obj, directory)}: {os.path.relpath(src, directory)}\n\t@echo \'Building file: $<\'\n\t@echo \'Invoking: Standard S32DS C Compiler\'\n\t${{TC_CC}} "@{obj}.args" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"\n\t@echo \'Finished building: $<\'\n\t@echo \' \'\n\n' for src, obj in zip(c_srcs, objs)) + """  
"""  
'''


compile_template = '''
{object_dir}/%.o: {src_dir}/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Standard S32DS C Compiler'
	${{TC_CC}} "@{args}" -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '
'''


def generate_makefile_mk(directory, make_relative_path, default_args):  
    make_path = os.path.join('./build', directory) #.replace('\./', '/')
    if not os.path.exists(make_path):
        os.makedirs(make_path)
    makefile_mk_name = os.path.join(make_path, 'subdir.mk')  
    # print(make_path)
    c_srcs = []  
    objs = []  
    c_deps = []  
      
    compile_setting_file = os.path.join(make_path, 'default.args')
    with open(compile_setting_file, 'w') as f:
        f.write(default_args)
        f.close()
    
    get_dir = list()
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
            dep_file = os.path.splitext(relative_path)[0] + '.d'  
            c_deps.append(dep_file) 
            # get_dir.append(root.replace('\\', '/'))
            all_objs.append(os.path.join(directory, obj_file).replace('\\', '/'))

    # 生成subdir.mk文件内容  
    makefile_mk_content = """  
# Automatically-generated file. Do not edit!  
  
C_SRCS += \\
""" + '\n'.join('    ' + os.path.join(make_relative_path, directory, src).replace('\\', '/') + ' \\' for src in c_srcs) + """
  
OBJS += \\
""" + '\n'.join('    ' + os.path.join(directory, obj).replace('\\', '/') + ' \\' for obj in objs) + """
  
C_DEPS += \\
""" + '\n'.join('    ' + os.path.join(directory, dep).replace('\\', '/') + ' \\' for dep in c_deps) + '\n'
    # compile_template_str = compile_template.format(object_dir = os.path.join(os.path.relpath( os.path.dirname(os.path.abspath(directory)), (os.path.abspath(all_root)) ), directory), src_dir = os.path.join(os.path.relpath( os.path.dirname(os.path.abspath(directory)), (os.path.abspath(all_root)) ), directory))
    # RTD/src/default.args
    # relpath = os.path.relpath( os.path.dirname(os.path.abspath(directory)), (os.path.abspath(all_root)) )
    # compile_template_str = compile_template.format(object_dir = os.path.join(os.path.relpath( os.path.dirname(os.path.abspath(directory)), (os.path.abspath(all_root)) ), directory), src_dir = os.path.join(os.path.relpath( os.path.dirname(os.path.abspath(directory)), (os.path.abspath(all_root)) ), directory))
    compile_template_str = compile_template.format(object_dir = directory, src_dir = os.path.join(make_relative_path, directory), args=os.path.join(directory, 'default.args')).replace('\\', '/')
    makefile_mk_content+= compile_template_str.replace('\\', '/')
    

    # print('xxxxxxxxxxxxxxxxxxx', make_relative_path, directory, compile_template_str.replace('/', '\\'))
    # print('xxxxxxxxxxxxxxxxxxx', compile_template_str.replace('\\', '/'), relpath, directory)
    # 将内容写入subdir.mk文件  
    with open(makefile_mk_name, 'w') as makefile_mk:  
        makefile_mk.write(makefile_mk_content)  
  
skip_list = ['Debug_FLASH', 'build', '.settings', 'Project_Settings']  
  
def foreach_dir(root_dir, relative_path, default_args):  
    get_dir = list()
    for root, dirs, files in os.walk(root_dir):  
        try:
            if not '__pycache__' in dirs :
                    dirs.remove('__pycache__')  
        except Exception as e:
            pass

        # if (not 'Debug_FLASH' in skip_list) and (not 'build' in root) and (not 'Project_Settings' in root):
        is_make = True
        is_have_c = False
        for ele in skip_list:
            if(ele in root):
                is_make = False
                
        for file in files:  
            if file.endswith('.c'):
                is_have_c = True
        if (is_make) and (is_have_c):
            # print(root, dirs, files)
            # input('wait aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            generate_makefile_mk(root, relative_path, default_args)  
            '''
            include_mk = '-include {0}'.format(root+'.mk')
            print('include', include_mk)
            '''
            get_dir.append(root.replace('\\', '/'))
            # generate_makefile_mk(root)  
    return get_dir
  
if __name__ == "__main__":  
    import argparse  
    parser = argparse.ArgumentParser(description='Generate Makefiles for each directory')  
    parser.add_argument("-r", type=str, help='The root directory to start traversal')
    parser.add_argument("-a", type=str, help='The compile default args path')    
    parser.add_argument("-m", type=str, help='The makefile template')   
    parser.add_argument("-l", type=str, help='The link parameter template')   
    
    args = parser.parse_args()  
    makefile_path = os.path.abspath('./Debug_FLASH')
    relative_path = os.path.relpath( os.path.abspath(args.r), makefile_path )  
    
    
    # print('xxxxxxxxxxxxxxx', makefile_path, os.path.abspath(args.r), relative_path)
    root_path = args.r
    
    with open(args.a, 'r') as f:
        default_args = f.read()
        
    dirs = foreach_dir(root_path, relative_path, default_args)
    # insert_content = str()
    insert_content_list = list()
    insert_content_list+= ('-include {0}'.format(dir_sub+'/subdir.mk\n') for dir_sub in dirs)
    insert_content = ''.join(insert_content_list)
    # print(dirs, insert_content)
    # for dir_sub in dirs:
        
    search_content = "-include Project_Settings/Startup_Code/subdir.mk"  
    with open(args.m, 'r') as f:  
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
        # print("create successful.")  
    else:  
        print("create fail")    
   
   
    search_content = '''"./Project_Settings/Startup_Code/system.o"'''   
    link_parameter_list = list()
    link_parameter_list+= ("\"{0}\"\n".format(obj) for obj in all_objs)
    link_parameter_content = ''.join(link_parameter_list)
    # print(link_parameter_list, link_parameter_content)
    link_lines = None
    with open(args.l, 'r') as f:  
        link_lines = f.readlines()  
    for i, line in enumerate(link_lines):  
        if search_content in line:  
            line_number = i  
            break  
            
    # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', i)
    if line_number is not None:  
        link_lines.insert(line_number + 1, link_parameter_content)              
        with open('./build/S32K3_M7_0_0.args', 'w') as file:  
            file.writelines(link_lines)  
            file.close()
    # os.system('cp ./config/compile.mk ./build/')
    subprocess.run(["powershell", 'cp ./config/compile.mk ./build/'], capture_output=True, text=True)
            
