from nuvolos_collect.distribute.utils import do_nothing, read_manifest, generate_target_info, execute_handback_copy

def distribute(source_folder):
    
    source_info = read_manifest(source_folder)
    target_info = generate_target_info(source_info)
    execute_handback_copy(target_info)
    