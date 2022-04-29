def list_services():
    import os
    from pathlib import Path
    current_path = os.getcwd()
    for file in os.listdir(current_path):
        if file.endswith(".pw"):
            print(Path(file).stem)
