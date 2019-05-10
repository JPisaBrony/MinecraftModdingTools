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

def createJsonFile(name, fileData):
    if not os.path.isfile(name) or args.override:
        with open(name, 'w') as file:
            file.write(json.dumps(fileData))
    else:
        print name + " not created since it exists. override with -override"

def createPngFile(name, textureLoc):
    png = name + ".png"
    png_loc =  MAIN_PATH + args.modid + textureLoc + png
    if not os.path.isfile(png_loc) or override:
        if os.path.isfile(png):
            os.rename(png, png_loc)
        else:
            print "creating json files without image in textures/block"
    else:
        print png_loc + " not created since it exists. override with -override"

def deleteFile(name):
    if os.path.isfile(name):
        os.remove(name)

if __name__ == '__main__':
    ID = args.modid
    DELETE = args.delete
    main_path_modid = MAIN_PATH + ID
    name = args.name
    if os.path.exists(main_path_modid):
        if args.type == "item":
            if DELETE == True:
                new_item_path = main_path_modid + "/models/item/" + name + ".json"
                deleteFile(new_item_path)
                png = main_path_modid + "/textures/item/" + name + ".png"
                deleteFile(png)
            else:
                itemJson = {}
                itemJson["parent"] = "item/generated"
                itemJson["textures"] = { "layer0": ID + ":item/" + name }
                new_item_path = main_path_modid + "/models/item/" + name + ".json"
                createJsonFile(new_item_path, itemJson)
                createPngFile(name, "/textures/item/")
        elif args.type == "block":
            if DELETE == True:
                bState = main_path_modid + "/blockstates/" + name + ".json"
                deleteFile(bState)
                new_block_path = main_path_modid + "/models/block/" + name + ".json"
                deleteFile(new_block_path)
                new_blockitem_path = main_path_modid + "/models/item/" + name + ".json"
                deleteFile(new_blockitem_path)
                png = main_path_modid + "/textures/block/" + name + ".png"
                deleteFile(png)
            else:
                blockState = {}
                blockJson = {}
                blockItem = {}
                blockState["variants"] = { "": {"model": ID + ":block/" + name }}
                blockJson["parent"] = "block/cube_all"
                blockJson["textures"] = { "all": ID + ":block/" + name }
                blockItem["parent"] = ID + ":block/" + name
                bState = main_path_modid + "/blockstates/" + name + ".json"
                createJsonFile(bState, blockState)
                new_block_path = main_path_modid + "/models/block/" + name + ".json"
                createJsonFile(new_block_path, blockJson)
                new_blockitem_path = main_path_modid + "/models/item/" + name + ".json"
                createJsonFile(new_blockitem_path, blockItem)
                createPngFile(name, "/textures/block/")
        else:
            print "type should be either 'item' or 'block'"
    else:
        print main_path_modid + " doesn't exist"
