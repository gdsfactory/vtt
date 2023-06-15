
__all__ = ["PATH"]

import pathlib

home = pathlib.Path.home()
cwd = pathlib.Path.cwd()

cwd_config = cwd / "config.yml"

home_config = home / ".config" / "vtt3um.yml"
config_dir = home / ".config"
config_dir.mkdir(exist_ok=True)
module_path = pathlib.Path(__file__).parent.absolute()
repo_path = module_path.parent


class Path:
    layer_lib = module_path / "VTT-layer-list.yaml"
    module = module_path
    repo = repo_path
    lyp = module_path / "klayout" / "layers.lyp"
    lyp_yaml = module_path / "klayout" / "layers.yaml"
    libs = module_path / "vtt3um"
    sparameters = module_path / "sparameters"

    libs_tech = libs / "libs.tech"
    libs_ref = libs / "libs.ref"
    libs_ngspice = libs_tech / "ngspice"

    gds = module_path / "gds"


PATH = Path()

if __name__ == "__main__":
    print(PATH)