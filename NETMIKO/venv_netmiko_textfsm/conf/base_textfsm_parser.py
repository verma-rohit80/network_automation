import textfsm,os,ntc_templates

class config_textfsm:
    PATH = os.path.join(
    "/home","rohit","Documents","python","Udemy","para_miko","para_virtual","NETMIKO","venv_netmiko_textfsm","CISCO_SHOW"
    )

    def textfsm_version(self,filename,template_file) -> list:
        filename = f"{config_textfsm.PATH}/{filename}"
        with open(filename) as f:
            f_read = f.read()        
        temp_vesion = []
        template_name = f"{ntc_templates.__path__[0]}/templates/{template_file}"
        template = open(template_name)
        re_table = textfsm.TextFSM(template)
        result = re_table.ParseText(f_read)
        return result
        