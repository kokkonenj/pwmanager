def list_services():
    import os
    from pathlib import Path
    current_path = os.getcwd()
    for file in os.listdir(current_path):
        if file.endswith(".pw"):
            print(Path(file).stem)


def file_exists(name):
    import os.path
    if os.path.exists(name):
        return True
    else:
        return False
