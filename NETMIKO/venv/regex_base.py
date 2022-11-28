import re,os

class Regex:

    def regex_version(self,filename):
        with open(filename) as f:
            f_ver = f.read()
        #  Code Version
        version_compile = re.compile(r"(?<=Version\s)(.+),",re.MULTILINE)
        result_version = version_compile.search(f_ver)
        

        # System image file
        version_image_file = re.compile(r""""(?<=file\sis\s\") # Capture (file is ")
                                              (.+)\"           # Capture everything until "
                                        """,re.M|re.VERBOSE)
        result_image_file = version_image_file.search(f_ver)
        
        # Capture uptime
        version_uptime = re.compile(r"(?<=uptime\sis\s)(.+)",re.MULTILINE)
        result_uptime = version_uptime.search(f_ver)

        # Capture Board ID
        version_board = re.compile(r"(?<=ID\s)(.+)",re.MULTILINE)
        result_board = version_board.search(f_ver)
 
        return [result_version.group(1),result_image_file.group(1),result_uptime.group(1),result_board.group(1)]

    def regex_run(self,filename):
        with open(filename) as f:
            f_run = f.read()
        # Hostname
        run_hostname = re.compile(r"hostname\s(.+)",re.MULTILINE)
        result_hostname = run_hostname.search(f_run)
        
        # Domain name
        run_domain = re.compile(r"domain\sname\s(.+)",re.MULTILINE)
        result_domain = run_domain.search(f_run)
        
        return [result_hostname.group(1),result_domain.group(1)]


    def regex_run_interfaces(self,filename):
        with open(filename) as f:
            f_run_int = f.read()

        run_int = re.compile(r"""interface\s(.+)\n                  # Capture everything after interface until \n
                                 (?:.+\n)?                          # If line with no ip address exists do not capture it
                                 \sip\saddress\s(.+)                # Capture eveything after ip address 
                                  """,re.M|re.VERBOSE)
        result_run_int = run_int.findall(f_run_int)
        return dict(result_run_int)

    def regex_route(self,filename):
        with open(filename) as f:
            f_route = f.read()
        route_compile = re.compile(r"""([CL])\s+             # start with C or L
                                        ([\d\.\/]+)          # capture IP address with mask
                                        .+,\s(.+)"""         #space until , and capture everything after it
                                        ,re.MULTILINE|re.VERBOSE)
        res_route = route_compile.findall(f_route)
        return res_route