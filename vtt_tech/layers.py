
import gdsfactory as gf
from gdsfactory.typings import Layer, LayerLevel, LayerStack
from pydantic import BaseModel, Extra

import yaml

from vtt_tech.config import PATH

class LayerMap(BaseModel):

    # waveguide types
    TYPE_RIB: Layer = (89, 0)
    TYPE_STRIP: Layer = (89, 1)

    # AUX
    FLOORPLAN: Layer = (63, 98)

    # common gdsfactory layers
    LABEL_INSTANCE: Layer = (66, 0)
    DEVREC: Layer = (68, 0)
    PORT: Layer = (99, 10)
    PORTE: Layer = (99, 11)
    TE: Layer = (203, 0)
    TM: Layer = (204, 0)
    TEXT: Layer = (66, 0)

    class Config:
        frozen = False
        extra = Extra.allow

LAYER = LayerMap()

# dynamically insert VTT layer entries from a YAML file.
with open(PATH.layer_lib, 'r') as file:
    data = yaml.safe_load(file)

    dadd = data['offsets']['add_offset']
    dsub = data['offsets']['sub_offset']
    dcpy = data['offsets']['cpy_offset']

    validate_list = []

    for mkey, module in data['modules'].items():
        gds_layer = module['gds_layer']
        for lname, layer in module['layers'].items():
            ld = (gds_layer, layer['datatype'])
            assert ld not in validate_list, f"Duplicate GDS layer/datatype definition for layer f'{mkey}_{lname}"
            validate_list.append(ld)

            setattr(LAYER, f'{mkey}_{lname}_ADD', tuple((gds_layer, dadd + layer['datatype'])))
            setattr(LAYER, f'{mkey}_{lname}_SUB', tuple((gds_layer, dsub + layer['datatype'])))
            setattr(LAYER, f'{mkey}_{lname}_CPY', tuple((gds_layer, dcpy + layer['datatype'])))

    gds_layer = data['aux']['gds_layer']
    mkey = data['aux']['id']
    for lname, layer in data['aux']['layers'].items():
        ld = (gds_layer, layer['datatype'])
        assert ld not in validate_list, f"Duplicate GDS layer/datatype definition for layer f'{mkey}_{lname}"
        validate_list.append(ld)

        setattr(LAYER, f'{mkey}_{lname}', tuple((gds_layer, layer['datatype'])))

# Prevent adding further layer definitions
LAYER.Config.frozen = True
LAYER.Config.extra = Extra.forbid


#LAYER_VIEWS = gf.technology.LayerViews(filepath=PATH.lyp_yaml)


if __name__ == "__main__":
    print(LAYER)
