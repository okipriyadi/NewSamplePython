from ConfigParser import SafeConfigParser
cfg_parser = SafeConfigParser()
cfg_parser.add_section('certificate')
cfg_parser.set('certificate', 'commonname', "Saya")
cfg_parser.set('certificate', 'not_before', "87")
cfg_parser.set('certificate', 'not_after', "2100")
cfg_parser.set('certificate', 'digest', "12345")
cfg_parser.write("disavedisini.ini")