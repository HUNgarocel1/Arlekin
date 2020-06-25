import uiScriptLocale
import item

EQUIPMENT_START_INDEX = 180
LOCALE_PATH = "locale/ro/ui/inventory_button/"

window = {
	"name" : "InventoryWindow",
	
	## 600 - (width + 오른쪽으로 부터 띄우기 24 px) 568
	"x" : SCREEN_WIDTH - 180,
	"y" : SCREEN_HEIGHT - 37 - 610,
	
	"style" : ("movable", "float",),
	
	"width" : 176,
	"height" : 568,
	
	"children" :
	(
		## Inventory, Equipment Slots
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
	
			"x" : 0,
			"y" : 0,
	
			"width" : 176,
			"height" : 568,
	
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
	
					"x" : 8,
					"y" : 7,
	
					"width" : 161,
					"color" : "yellow",
	
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":77, "y":3, "text":uiScriptLocale.INVENTORY_TITLE, "text_horizontal_align":"center" },
					),
				},
				## Equipment Slot
				{
					"name" : "Equipment_Base",
					"type" : "image",
					"x" : 10,
					"y" : 33,
					"image" : "d:/ymir work/ui/equipment_bg_wit_pet1.png",
					"children" :
					(
						{
							"name" : "EquipmentSlot",
							"type" : "slot",
	
							"x" : 3,
							"y" : 3,
	
							"width" : 150,
							"height" : 217,
	
							"slot" : (
										{"index":EQUIPMENT_START_INDEX+0, "x":39, "y":37, "width":32, "height":64},
										{"index":EQUIPMENT_START_INDEX+1, "x":39, "y":2, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+2, "x":39, "y":145, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+3, "x":75, "y":67, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+4, "x":3, "y":3, "width":32, "height":96},
										{"index":EQUIPMENT_START_INDEX+5, "x":114, "y":67, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+6, "x":114, "y":35, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+7, "x":2, "y":145, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+8, "x":75, "y":145, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+9, "x":114, "y":2, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+10, "x":75, "y":35, "width":32, "height":32},
										{"index":item.EQUIPMENT_RING1, "x":2, "y":106, "width":32, "height":32},
										{"index":item.EQUIPMENT_BELT, "x":39, "y":106, "width":32, "height":32},
										{"index":item.EQUIPMENT_PET , "x":75, "y":106, "width":32, "height":32},
										{"index":item.EQUIPMENT_TITLE , "x":0, "y":180, "width":32, "height":32},
										{"index":item.EQUIPMENT_BUFF , "x":38, "y":180, "width":32, "height":32},
									),
						},
						{
							"name" : "DSSButton",
							"type" : "button",
						
							"x" : 114,
							"y" : 104,

							"tooltip_text" : "Alchimie Piatra Dragon",
						
							"default_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_01.tga",
							"over_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_02.tga",
							"down_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_03.tga",
						},
						{
							"name" : "OFFButton",
							"type" : "button",

							# "x" : 77,
							# "y" : 110,
							"x" : 116,
							"y" : 145,

							"tooltip_text" : "Magazin Privat",

							"default_image" : LOCALE_PATH+"private_button_01.tga",
							"over_image" : LOCALE_PATH+"private_button_02.tga",
							"down_image" : LOCALE_PATH+"private_button_01.tga",
						},
						{
							"name" : "SWITCHButton",
							"type" : "button",

							"x" : 76,
							"y" : 180,

							"tooltip_text" : "Depozit Special",

							"default_image" : LOCALE_PATH+"depozit_special_2.png",
							"over_image" : LOCALE_PATH+"depozit_special.png",
							"down_image" : LOCALE_PATH+"depozit_special_2.png",
						},
						{
							"name" : "INFOCHESTButton",
							"type" : "button",

							"x" : 114,
							"y" : 180,

							"tooltip_text" : "Meniu",

							"default_image" : LOCALE_PATH+"mcard_button_01.png",
							"over_image" : LOCALE_PATH+"mcard_button_02.png",
							"down_image" : LOCALE_PATH+"mcard_button_01.png",
						},
						## CostumeButton
						{
							"name" : "CostumeButton",
							"type" : "button",
	
							"x" : 78,
							"y" : 5,
	
							"tooltip_text" : uiScriptLocale.COSTUME_TITLE,
	
							"default_image" : "d:/ymir work/ui/game/taskbar/costume_Button_01.tga",
							"over_image" : "d:/ymir work/ui/game/taskbar/costume_Button_02.tga",
							"down_image" : "d:/ymir work/ui/game/taskbar/costume_Button_03.tga",
						},                       
						{
							"name" : "Equipment_Tab_01",
							"type" : "radio_button",

							"x" : 86,
							# "y" : 161,
							"y" : 215,

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

							"children" :
							(
								{
									"name" : "Equipment_Tab_01_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "I",
								},
							),
						},
						{
							"name" : "Equipment_Tab_02",
							"type" : "radio_button",

							"x" : 86 + 32,
							"y" : 215,

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

							"children" :
							(
								{
									"name" : "Equipment_Tab_02_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "II",
								},
							),
						},

					),
				},

				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",
					"x" : 10,
					"y" : 33 + 215,
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,
					"children" :
					(
					    {
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"all_align" : "center",
							"text" : "I",
					    },
					),
				},
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",
					"x" : 10 + 39,
					"y" : 33 + 215,
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,
					"children" :
					(
					    {
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"all_align" : "center",
							"text" : "II",
					    },
					),
				},
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",
					"x" : 10 + 39 + 39,
					"y" : 33 + 215,
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,
					"children" :
					(
					    {
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"all_align" : "center",
							"text" : "III",
					    },
					),
				},
				{
					"name" : "Inventory_Tab_04",
					"type" : "radio_button",
					"x" : 10 + 39 + 39 + 39,
					"y" : 33 + 215,
					"default_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_01.sub",
					"over_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_02.sub",
					"down_image" : "d:/ymir work/ui/game/windows/tab_button_large_half_03.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_4,
					"children" :
					(
					    {
							"name" : "Inventory_Tab_04_Print",
							"type" : "text",
							"x" : 0,
							"y" : 0,
							"all_align" : "center",
							"text" : "IV",
					    },
					),
				},
				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",
	
					"x" : 8,
					"y" : 266,
	
					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 9,
					"x_step" : 32,
					"y_step" : 32,
	
					"image" : "d:/ymir work/ui/public/Slot_Base.sub"
				},	
			),
		},
	),
}