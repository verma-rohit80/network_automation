folder conf:
	class for base_main_config.py to extablish connection and pull output from box
	class for base_textfsm_parser.py to parse show commands
	
config.puller.py : imports base_main_config.py and pulls config
config_parsr.py  : imports class of base_textfsm_parser.py and parse show commands and present in a table
