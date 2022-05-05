import re
source_ip = "1.2.3.4/32,5.6.7.8/27"
cidrs = re.split(r"\n |,", source_ip)
print(cidrs)
#Adding comment
