import re,os

class Regex_Parser:

    def version(self,file_version):
        """
        Capture uptime,board ID,
        """
        file_name = file_version.split("__")[0]
        with open(file_version) as f:
            file_version = f.read()
        uptime_compile = re.compile(r"(?<=uptime\sis\s).+")
        uptime = uptime_compile.search(file_version).group()

        board_compile = re.compile(r"(?<=board\sID\s).+")
        board = board_compile.search(file_version).group()

        image_compile = re.compile(r"flash.+")
        image = image_compile.search(file_version).group()

        return [file_name,uptime,board,image]

    def run_interface(self,file_run):
        file_name = file_run.split("__")[0]
        with open(file_run) as f:
            file_run = f.read()
        
        run_interface_compile = re.compile(r"(interface .+)\n(?:\s.+\n)?\s(ip\saddress.+)",re.MULTILINE)
        run_interfaces = run_interface_compile.findall(file_run)
        return [file_name,dict(run_interfaces)]

    def interface_brief(self,file_brief):
        file_name = file_brief.split("__")[0]
        with open(file_brief) as f:
            file_brief = f.read()

        brief_compile = re.compile(r"(\S+)\s+([\d.]+)\s+YES+\sNVRAM\s+(\w+)")
        interfaces_brief = brief_compile.findall(file_brief)
        return [file_name,interfaces_brief]
    



