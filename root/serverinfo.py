import net
(sv1_ip, sv1_name) = net.GetServer_IPNAME()
(ch1_port, ch2_port, ch3_port, ch4_port, auth_port, mark_port) = net.GetServer_PORT()

CH_1_NAME	= "|cFF00FFFF|hCH1"
CH_2_NAME	= "|cFF00FFFF|hCH2"
CH_3_NAME	= "|cFF00FFFF|hCH3"
CH_4_NAME	= "|cFF00FFFF|hCH4"

STATE_NONE = "|cFFFF0000|hZÁRVA"
	
STATE_DICT = {
	0 : "|cFFFF0000|hZÁRVA",
	1 : "|cff00ff00|hNORMAL",
	2 : "|cff00ff00|hKÖZÉP",
	3 : "|cff00ff00|hTELE"
}

SERVER01_CHANNEL_DICT = {
	1:{"key":11,"name":CH_1_NAME,"ip":sv1_ip,"tcp_port":ch1_port,"udp_port":ch1_port,"state":STATE_NONE,},
	2:{"key":12,"name":CH_2_NAME,"ip":sv1_ip,"tcp_port":ch2_port,"udp_port":ch2_port,"state":STATE_NONE,},
	3:{"key":13,"name":CH_3_NAME,"ip":sv1_ip,"tcp_port":ch3_port,"udp_port":ch3_port,"state":STATE_NONE,},
	4:{"key":14,"name":CH_4_NAME,"ip":sv1_ip,"tcp_port":ch4_port,"udp_port":ch4_port,"state":STATE_NONE,},
}

REGION_NAME_DICT = {
	0 : "",	
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { "ip":sv1_ip, "port":auth_port, },
	}		
}

REGION_DICT = {
	0 : {
		1 : { "name" :sv1_name, "channel" : SERVER01_CHANNEL_DICT, },
	},
}

MARKADDR_DICT = {
	10 : { "ip" : sv1_ip, "tcp_port" : mark_port, "mark" : "10.tga", "symbol_path" : "10", },
}