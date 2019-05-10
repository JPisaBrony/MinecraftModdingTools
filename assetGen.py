import argparse
import os
import json

MAIN_PATH = "src/main/resources/assets/"

parser = argparse.ArgumentParser()
parser.add_argument("-modid", required=True)
parser.add_argument("-type", required=True)
parser.add_argument("-name", required=True)
parser.add_argument("-delete", action='store_true')
parser.add_argument("-override", action='store_true')
args = parser.parse_args()

if __name__ == '__main__':
    ID = args.modid
    name = args.name
    delete = args.delete
    override = args.override
    OVERRIDE_MSG = " not created since it exists. override with -override"
    main_path_modid = MAIN_PATH + ID
    if os.path.exists(main_path_modid):
        if args.type == "item":
            itemJson = {}
            itemJson["parent"] = "item/generated"
            itemJson["textures"] = { "layer0": ID + ":item/" + name }
            new_item_path = main_path_modid + "/models/item/" + name + ".json"
            with open(new_item_path, 'w') as file:
                file.write(json.dumps(itemJson))
        elif args.type == "block":
            if delete == True:
                bState = main_path_modid + "/blockstates/" + name + ".json"
                if os.path.isfile(bState):
                    os.remove(bState)
                new_block_path = main_path_modid + "/models/block/" + name + ".json"
                if os.path.isfile(new_block_path):
                    os.remove(new_block_path)
                new_blockitem_path = main_path_modid + "/models/item/" + name + ".json"
                if os.path.isfile(new_blockitem_path):
                    os.remove(new_blockitem_path)
                png = main_path_modid + "/textures/block/" + name + ".png"
                if os.path.isfile(png):
                    os.remove(png)
            else:
                blockState = {}
                blockJson = {}
                blockItem = {}
                blockState["variants"] = { "": {"model": ID + ":block/" + name }}
                blockJson["parent"] = "block/cube_all"
                blockJson["textures"] = { "all": ID + ":block/" + name }
                blockItem["parent"] = ID + ":block/" + name
                bState = main_path_modid + "/blockstates/" + name + ".json"
                if not os.path.isfile(bState) or override:
                    with open(bState, 'w') as file:
                        file.write(json.dumps(blockState))
                else:
                    print bState + OVERRIDE_MSG
                
                new_block_path = main_path_modid + "/models/block/" + name + ".json"
                if not os.path.isfile(new_block_path) or override:
                    with open(new_block_path, 'w') as file:
                        file.write(json.dumps(blockJson))
                else:
                    print new_block_path + OVERRIDE_MSG
                
                new_blockitem_path = main_path_modid + "/models/item/" + name + ".json"
                if not os.path.isfile(new_blockitem_path) or override:
                    with open(new_blockitem_path, 'w') as file:
                        file.write(json.dumps(blockItem))
                else:
                    print new_blockitem_path + OVERRIDE_MSG
                
                png = name + ".png"
                png_loc = main_path_modid + "/textures/block/" + png
                if not os.path.isfile(png_loc) or override:
                    if os.path.isfile(png):
                        os.rename(png, png_loc)
                    else:
                        print "creating json files without image in textures/block"
                else:
                    print png_loc + OVERRIDE_MSG
        else:
            print "type should be either 'item' or 'block'"
    else:
        print main_path_modid + " doesn't exist"
