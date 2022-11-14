import re,os

class Regex_parser:

    def show_version_parser(self,filename):
        uptime_compile = re.compile(r"(?<=uptime\sis)\s(.+)")
        uptime = uptime_compile.search(filename).group()
        
        board_compile= re.compile(r"(?<=board\sID\s)(.+)")
        board = board_compile.search(filename).group()
        return uptime,board

    def show_run_parser(self,filename):
        hostname_compile = re.compile(r"(?<=hostname\s)(.+)")
        hostname = hostname_compile.search(filename).group()
        
        domain_compile = re.compile(r"(?<=domain\sname\s)(.+)")
        domain = domain_compile.search(filename).group()
        return hostname,domain

    def show_run_interface_parser(self,filename):
        interfaces_compile = re.compile(r"(interface\s.+)\n(?:.+\n)?\s?(ip\s.+)")
        interfaces = interfaces_compile.findall(filename)
        return interfaces





