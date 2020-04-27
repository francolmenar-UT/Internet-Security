raw_folder = "raw_input/"
pre_folder = "preprocessed_input/"
post_folder = "processed_input/"
huge_folder = "huge/"
huge_file = "huge.txt"


flow_st = "Date flow start"

nf_r = "nfdump -r "

old_header = ["Date flow start", "Duration", "Proto", "Src IP Addr:Port",
                   "Dst IP Addr:Port", "Packets", "Bytes", "Flows"]

no_space_header = ["Date_flow_start", "Duration", "Proto", "Src_IP_Addr:Port",
                   "Dst_IP_Addr:Port", "Packets", "Bytes", "Flows"]

new_header = ["Date_flow_start", "Hour_flow_start", "Duration", "Proto", "Src_IP_Addr:Port",
                   "Dst_IP_Addr:Port", "Packets", "Bytes", "Flows"]