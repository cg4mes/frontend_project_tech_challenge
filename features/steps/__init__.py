import os
import importlib
import pkgutil

__all__ = []
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

# Recorremos todos los subdirectorios dentro de 'steps'
for root, dirs, files in os.walk(CURRENT_PATH):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        if os.path.isdir(dir_path):
            # Recorremos los módulos dentro de cada subdirectorio
            for module_info in pkgutil.iter_modules([dir_path]):
                module_name = f"{dir_name}.{module_info.name}"
                __all__.append(module_name)
                try:
                    # Importamos explícitamente el módulo
                    module = importlib.import_module(module_name)
                    globals()[module_name] = module
                except ModuleNotFoundError as e:
                    print(f"Error importing module {module_name}: {e}")
