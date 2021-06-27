
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI
def clo1():
    net = Mininet()
    #definisi host
    r1 = net.addHost("r1")
    r2 = net.addHost("r2")
    r3 = net.addHost("r3")
    r4 = net.addHost("r4")
    h1 = net.addHost("h1")
    h2 = net.addHost("h2")
    #penyambungan link atau subnetting
    net.addLink(h1,r1,intfName1='h1-eth0',intfName2='r1-eth0',cls = TCLink,bw=1)
    net.addLink(h1,r2,intfName1='h1-eth1',intfName2='r2-eth0',cls = TCLink,bw=1)
    net.addLink(h2,r3,intfName1='h2-eth0',intfName2='r3-eth0',cls = TCLink,bw=1)
    net.addLink(h2,r4,intfName1='h2-eth1',intfName2='r4-eth0',cls = TCLink,bw=1)
    net.addLink(r1,r3,intfName1='r1-eth1',intfName2='r3-eth1',cls = TCLink,bw=0.5)
    net.addLink(r1,r4,intfName1='r1-eth2',intfName2='r4-eth1',cls = TCLink,bw=1)
    net.addLink(r2,r3,intfName1='r2-eth1',intfName2='r3-eth2',cls = TCLink,bw=1)
    net.addLink(r2,r4,intfName1='r2-eth2',intfName2='r4-eth2',cls = TCLink,bw=0.5)
    net.start()
    
    # Konfigurasi IP Address di host 1 dan 2
    h1.cmd("ifconfig h1-eth0 192.168.0.2/24 netmask 255.255.255.0")
    h1.cmd("ifconfig h1-eth1 192.168.1.2/24 netmask 255.255.255.0")
    h2.cmd("ifconfig h2-eth0 192.168.2.2/24 netmask 255.255.255.0")
    h2.cmd("ifconfig h2-eth1 192.168.3.2/24 netmask 255.255.255.0")
    
    # konfigurasi Router
    r1.cmd("ifconfig r1-eth0 192.168.0.1/24 netmask 255.255.255.0")
    r1.cmd("ifconfig r1-eth1 192.168.4.1/24 netmask 255.255.255.0")
    r1.cmd("ifconfig r1-eth2 192.168.5.2/24 netmask 255.255.255.0")
    r1.cmd("sysctl net.ipv4.ip_forward=1")
    
    r2.cmd("ifconfig r2-eth0 192.168.1.1/24 netmask 255.255.255.0")
    r2.cmd("ifconfig r2-eth1 192.168.6.2/24 netmask 255.255.255.0")
    r2.cmd("ifconfig r2-eth2 192.168.7.1/24 netmask 255.255.255.0")
    r2.cmd("sysctl net.ipv4.ip_forward=1")

    r3.cmd("ifconfig r3-eth0 192.168.2.1/24 netmask 255.255.255.0")
    r3.cmd("ifconfig r3-eth1 192.168.4.2/24 netmask 255.255.255.0")
    r3.cmd("ifconfig r3-eth2 192.168.6.1/24 netmask 255.255.255.0")
    r3.cmd("sysctl net.ipv4.ip_forward=1")

    #routing

    r4.cmd("ifconfig r4-eth0 192.168.3.1/24 netmask 255.255.255.0")
    r4.cmd("ifconfig r4-eth1 192.168.5.1/24 netmask 255.255.255.0")
    r4.cmd("ifconfig r4-eth2 192.168.7.2/24 netmask 255.255.255.0")
    r4.cmd("sysctl net.ipv4.ip_forward=1")
    
    print("TES PING H1 - R1")
    h1.cmdPrint("ping -c 3 192.168.0.1")
    print("\n")
    print("TES PING R1 - H1")
    r1.cmdPrint("ping -c 3 192.168.0.2")
    print("\n")

    print("TES PING H1 - R2")
    h1.cmdPrint("ping -c 3 192.168.1.1")
    print("\n")
    print("TES PING R2 - H1")
    r2.cmdPrint("ping -c 3 192.168.1.2")
    print("\n")

    print("TES PING H2 - R3")
    h2.cmdPrint("ping -c 3 192.168.2.1")
    print("\n")
    print("TES PING R3 - H2")
    r3.cmdPrint("ping -c 3 192.168.2.2")
    print("\n")

    print("TES PING H2 - R4")
    h2.cmdPrint("ping -c 3 192.168.3.1")
    print("\n")
    print("TES PING R4 - H2")
    r4.cmdPrint("ping -c 3 192.168.3.2")
    print("\n")

    print("TES PING R1 - R3")
    r1.cmdPrint("ping -c 3 192.168.5.1")
    print("\n")
    print("TES PING R3 - R1")
    r3.cmdPrint("ping -c 3 192.168.5.2")
    print("\n")


    print("TES PING R1 - R4")
    r1.cmdPrint("ping -c 3 192.168.4.2")
    print("\n")
    print("TES PING R4 - R1")
    r4.cmdPrint("ping -c 3 192.168.4.1")
    print("\n")


    print("TES PING R2 - R3")
    r2.cmdPrint("ping -c 3 192.168.6.1")
    print("\n")
    print("TES PING R3 - R2")
    r3.cmdPrint("ping -c 3 192.168.6.2")
    print("\n")

    print("TES PING R2 - R4")
    r2.cmdPrint("ping -c 3 192.168.7.1")
    print("\n")
    print("TES PING R4 - R2")
    r4.cmdPrint("ping -c 3 192.168.7.2")
    print("\n")

    CLI(net)
    net.stop()
    
def clo2_3():

    net = Mininet()
    #definisi Host
    r1 = net.addHost("r1")
    r2 = net.addHost("r2")
    r3 = net.addHost("r3")
    r4 = net.addHost("r4")
    h1 = net.addHost("h1")
    h2 = net.addHost("h2")
    #penyambungan link atau subnetting
    net.addLink(h1,r1,intfName1='h1-eth0',intfName2='r1-eth0',cls = TCLink,bw=1)
    net.addLink(h1,r2,intfName1='h1-eth1',intfName2='r2-eth0',cls = TCLink,bw=1)
    net.addLink(h2,r3,intfName1='h2-eth0',intfName2='r3-eth0',cls = TCLink,bw=1)
    net.addLink(h2,r4,intfName1='h2-eth1',intfName2='r4-eth0',cls = TCLink,bw=1)
    net.addLink(r1,r3,intfName1='r1-eth1',intfName2='r3-eth1',cls = TCLink,bw=0.5)
    net.addLink(r1,r4,intfName1='r1-eth2',intfName2='r4-eth1',cls = TCLink,bw=1)
    net.addLink(r2,r3,intfName1='r2-eth1',intfName2='r3-eth2',cls = TCLink,bw=1)
    net.addLink(r2,r4,intfName1='r2-eth2',intfName2='r4-eth2',cls = TCLink,bw=0.5)
    net.start()
    
    # Konfigurasi IP Address di host 1 dan 2
    h1.cmd("ifconfig h1-eth0 192.168.0.2/24 netmask 255.255.255.0")
    h1.cmd("ifconfig h1-eth1 192.168.1.2/24 netmask 255.255.255.0")
    h2.cmd("ifconfig h2-eth0 192.168.2.2/24 netmask 255.255.255.0")
    h2.cmd("ifconfig h2-eth1 192.168.3.2/24 netmask 255.255.255.0")
    
    #routing h1 dan h2

    h1.cmd("ip rule add from 192.168.0.2 table 1")
    h1.cmd("ip rule add from 192.168.1.2 table 2")

    h1.cmd("ip route add 192.168.0.0/24 dev h1-eth0 link table 1")
    h1.cmd("ip route add default via 192.168.0.1 dev h1-eth0 table 1")
    h1.cmd("ip route add 192.168.1.0/24 dev h1-eth0 link table 2")
    h1.cmd("ip route add default via 192.168.1.1 dev h1-eth1 table 2")
    h1.cmd("ip route add default scope global nexthop via 192.168.0.1 dev h1-eth0")
    h1.cmd("ip route add default scope global nexthop via 192.168.1.1 dev h1-eth1")
    
    #h1.cmd("route add default gw 192.168.0.1 h1-eth0")
    #h1.cmd("route add default gw 192.168.1.1 h1-eth1")

    h2.cmd("ip rule add from 192.168.2.2 table 3")
    h2.cmd("ip rule add from 192.168.3.2 table 4")
    h2.cmd("ip route add 192.168.2.0/24 dev h2-eth0 link table 3")
    h2.cmd("ip route add default via 192.168.2.1 dev h2-eth0 table 3")
    h2.cmd("ip route add 192.168.3.0/24 dev h2-eth0 link table 4")
    h2.cmd("ip route add default via 192.168.3.1 dev h2-eth1 table 4")
    h2.cmd("ip route add default scope global nexthop via 192.168.2.1 dev h2-eth0")
    h2.cmd("ip route add default scope global nexthop via 192.168.3.1 dev h2-eth1")
    #h2.cmd("route add default gw 192.168.2.1 h2-eth0")
    #h2.cmd("route add default gw 192.168.3.1 h2-eth1")
    
    #Konfigurasi Router dan Routing Static
    r1.cmd("ifconfig r1-eth0 192.168.0.1/24 netmask 255.255.255.0")
    r1.cmd("ifconfig r1-eth1 192.168.4.1/24 netmask 255.255.255.0")
    r1.cmd("ifconfig r1-eth2 192.168.5.2/24 netmask 255.255.255.0")
    r1.cmd("sysctl net.ipv4.ip_forward=1")

    r1.cmd("route add -net 192.168.1.0/24 gw 192.168.5.1")
    r1.cmd("route add -net 192.168.1.0/24 gw 192.168.4.2")
    r1.cmd("route add -net 192.168.2.0/24 gw 192.168.4.2")
    r1.cmd("route add -net 192.168.3.0/24 gw 192.168.5.1")
    r1.cmd("route add -net 192.168.6.0/24 gw 192.168.4.2")
    r1.cmd("route add -net 192.168.7.0/24 gw 192.168.5.1")
    
    r2.cmd("ifconfig r2-eth0 192.168.1.1/24 netmask 255.255.255.0")
    r2.cmd("ifconfig r2-eth1 192.168.6.2/24 netmask 255.255.255.0")
    r2.cmd("ifconfig r2-eth2 192.168.7.1/24 netmask 255.255.255.0")
    r2.cmd("sysctl net.ipv4.ip_forward=1")

    r2.cmd("route add -net 192.168.0.0/24 gw 192.168.6.1")
    r2.cmd("route add -net 192.168.0.0/24 gw 192.168.7.2")
    r2.cmd("route add -net 192.168.2.0/24 gw 192.168.6.1")
    r2.cmd("route add -net 192.168.3.0/24 gw 192.168.7.2")
    r2.cmd("route add -net 192.168.4.0/24 gw 192.168.6.1")
    r2.cmd("route add -net 192.168.5.0/24 gw 192.168.7.2")

    r3.cmd("ifconfig r3-eth0 192.168.2.1/24 netmask 255.255.255.0")
    r3.cmd("ifconfig r3-eth1 192.168.4.2/24 netmask 255.255.255.0")
    r3.cmd("ifconfig r3-eth2 192.168.6.1/24 netmask 255.255.255.0")
    r3.cmd("sysctl net.ipv4.ip_forward=1")

    r3.cmd("route add -net 192.168.0.0/24 gw 192.168.4.1")
    r3.cmd("route add -net 192.168.1.0/24 gw 192.168.6.2")
    r3.cmd("route add -net 192.168.3.0/24 gw 192.168.6.2")
    r3.cmd("route add -net 192.168.3.0/24 gw 192.168.4.1")
    r3.cmd("route add -net 192.168.7.0/24 gw 192.168.6.2")
    r3.cmd("route add -net 192.168.5.0/24 gw 192.168.4.1")

    r4.cmd("ifconfig r4-eth0 192.168.3.1/24 netmask 255.255.255.0")
    r4.cmd("ifconfig r4-eth1 192.168.5.1/24 netmask 255.255.255.0")
    r4.cmd("ifconfig r4-eth2 192.168.7.2/24 netmask 255.255.255.0")
    r4.cmd("sysctl net.ipv4.ip_forward=1")

    r4.cmd("route add -net 192.168.0.0/24 gw 192.168.5.2")
    r4.cmd("route add -net 192.168.1.0/24 gw 192.168.7.1")
    r4.cmd("route add -net 192.168.2.0/24 gw 192.168.7.1")
    r4.cmd("route add -net 192.168.2.0/24 gw 192.168.5.2")
    r4.cmd("route add -net 192.168.6.0/24 gw 192.168.7.1")
    r4.cmd("route add -net 192.168.4.0/24 gw 192.168.5.2")
    
    
    print("TES PING R1 - R2")
    r1.cmdPrint("ping -c 3 192.168.6.2")
    print("\n")
    print("TES PING R3 - R4")
    r3.cmdPrint("ping -c 3 192.168.4.2")
    print("\n")
    

    print("TES PING H1 - H2 interface Atas")
    h1.cmdPrint("ping -c 3 192.168.2.2")
    print("\n")
    print("TES PING H1- H2 interface Bawah")
    h1.cmdPrint("ping -c 3 192.168.3.2")
    print("\n")
    print("TES PING H2 - H1 interface Atas")
    h2.cmdPrint("ping -c 3 192.168.0.2")
    print("\n")
    print("TES PING H2- H1 interface Bawah")
    h2.cmdPrint("ping -c 3 192.168.1.2")
    print("\n")
    

    CLI(net)
    net.stop()
def clo4(buffer):

    net = Mininet()
    #definisi host
    r1 = net.addHost("r1")
    r2 = net.addHost("r2")
    r3 = net.addHost("r3")
    r4 = net.addHost("r4")
    h1 = net.addHost("h1")
    h2 = net.addHost("h2")

    buffer= int(buffer)
    #penyambungan link dan set buffer dan menggunakan queue HTB dengan static routing
    net.addLink(h1,r1,max_queue_size=buffer,use_htb=True,intfName1='h1-eth0',intfName2='r1-eth0',cls = TCLink,bw=1)
    net.addLink(h1,r2,max_queue_size=buffer,use_htb=True,intfName1='h1-eth1',intfName2='r2-eth0',cls = TCLink,bw=1)
    net.addLink(h2,r3,max_queue_size=buffer,use_htb=True,intfName1='h2-eth0',intfName2='r3-eth0',cls = TCLink,bw=1)
    net.addLink(h2,r4,max_queue_size=buffer,use_htb=True,intfName1='h2-eth1',intfName2='r4-eth0',cls = TCLink,bw=1)
    net.addLink(r1,r3,max_queue_size=buffer,use_htb=True,intfName1='r1-eth1',intfName2='r3-eth1',cls = TCLink,bw=0.5)
    net.addLink(r1,r4,max_queue_size=buffer,use_htb=True,intfName1='r1-eth2',intfName2='r4-eth1',cls = TCLink,bw=1)
    net.addLink(r2,r3,max_queue_size=buffer,use_htb=True,intfName1='r2-eth1',intfName2='r3-eth2',cls = TCLink,bw=1)
    net.addLink(r2,r4,max_queue_size=buffer,use_htb=True,intfName1='r2-eth2',intfName2='r4-eth2',cls = TCLink,bw=0.5)
    net.start()

  
    
    # Konfigurasi IP Address di host 1 dan 2
    h1.cmd("ifconfig h1-eth0 192.168.0.2/24 netmask 255.255.255.0")
    h1.cmd("ifconfig h1-eth1 192.168.1.2/24 netmask 255.255.255.0")
    h2.cmd("ifconfig h2-eth0 192.168.2.2/24 netmask 255.255.255.0")
    h2.cmd("ifconfig h2-eth1 192.168.3.2/24 netmask 255.255.255.0")
    
    
    #routing h1 h2

    h1.cmd("ip rule add from 192.168.0.2 table 1")
    h1.cmd("ip rule add from 192.168.1.2 table 2")
    h1.cmd("ip route add 192.168.0.0/24 dev h1-eth0 link table 1")
    h1.cmd("ip route add default via 192.168.0.1 dev h1-eth0 table 1")
    h1.cmd("ip route add 192.168.1.0/24 dev h1-eth0 link table 2")
    h1.cmd("ip route add default via 192.168.1.1 dev h1-eth1 table 2")
    h1.cmd("ip route add default scope global nexthop via 192.168.0.1 dev h1-eth0")
    h1.cmd("ip route add default scope global nexthop via 192.168.1.1 dev h1-eth1")
    #h1.cmd("route add -net default gw 192.168.0.1")
    #h1.cmd("route add -net default gw 192.168.1.1")
    
    h2.cmd("ip rule add from 192.168.2.2 table 3")
    h2.cmd("ip rule add from 192.168.3.2 table 4")
    h2.cmd("ip route add 192.168.2.0/24 dev h2-eth0 link table 3")
    h2.cmd("ip route add default via 192.168.2.1 dev h2-eth0 table 3")
    h2.cmd("ip route add 192.168.3.0/24 dev h2-eth0 link table 4")
    h2.cmd("ip route add default via 192.168.3.1 dev h2-eth1 table 4")
    h2.cmd("ip route add default scope global nexthop via 192.168.2.1 dev h2-eth0")
    h2.cmd("ip route add default scope global nexthop via 192.168.3.1 dev h2-eth1")
    #h2.cmd("route add default gw 192.168.2.1 h2-eth0")
    #h2.cmd("route add default gw 192.168.3.1 h2-eth1")
    

    #Konfigurasi Router dan Routing 

    r1.cmd("ifconfig r1-eth0 192.168.0.1/24 netmask 255.255.255.0")
    r1.cmd("ifconfig r1-eth1 192.168.4.1/24 netmask 255.255.255.0")
    r1.cmd("ifconfig r1-eth2 192.168.5.2/24 netmask 255.255.255.0")
    r1.cmd("sysctl net.ipv4.ip_forward=1")

    r1.cmd("route add -net 192.168.1.0/24 gw 192.168.5.1")
    r1.cmd("route add -net 192.168.1.0/24 gw 192.168.4.2")
    r1.cmd("route add -net 192.168.2.0/24 gw 192.168.4.2")
    r1.cmd("route add -net 192.168.3.0/24 gw 192.168.5.1")
    r1.cmd("route add -net 192.168.6.0/24 gw 192.168.4.2")
    r1.cmd("route add -net 192.168.7.0/24 gw 192.168.5.1")
    
    r2.cmd("ifconfig r2-eth0 192.168.1.1/24 netmask 255.255.255.0")
    r2.cmd("ifconfig r2-eth1 192.168.6.2/24 netmask 255.255.255.0")
    r2.cmd("ifconfig r2-eth2 192.168.7.1/24 netmask 255.255.255.0")
    r2.cmd("sysctl net.ipv4.ip_forward=1")

    r2.cmd("route add -net 192.168.0.0/24 gw 192.168.6.1")
    r2.cmd("route add -net 192.168.0.0/24 gw 192.168.7.2")
    r2.cmd("route add -net 192.168.2.0/24 gw 192.168.6.1")
    r2.cmd("route add -net 192.168.3.0/24 gw 192.168.7.2")
    r2.cmd("route add -net 192.168.4.0/24 gw 192.168.6.1")
    r2.cmd("route add -net 192.168.5.0/24 gw 192.168.7.2")

    r3.cmd("ifconfig r3-eth0 192.168.2.1/24 netmask 255.255.255.0")
    r3.cmd("ifconfig r3-eth1 192.168.4.2/24 netmask 255.255.255.0")
    r3.cmd("ifconfig r3-eth2 192.168.6.1/24 netmask 255.255.255.0")
    r3.cmd("sysctl net.ipv4.ip_forward=1")

    r3.cmd("route add -net 192.168.0.0/24 gw 192.168.4.1")
    r3.cmd("route add -net 192.168.1.0/24 gw 192.168.6.2")
    r3.cmd("route add -net 192.168.3.0/24 gw 192.168.6.2")
    r3.cmd("route add -net 192.168.3.0/24 gw 192.168.4.1")
    r3.cmd("route add -net 192.168.7.0/24 gw 192.168.6.2")
    r3.cmd("route add -net 192.168.5.0/24 gw 192.168.4.1")

    r4.cmd("ifconfig r4-eth0 192.168.3.1/24 netmask 255.255.255.0")
    r4.cmd("ifconfig r4-eth1 192.168.5.1/24 netmask 255.255.255.0")
    r4.cmd("ifconfig r4-eth2 192.168.7.2/24 netmask 255.255.255.0")
    r4.cmd("sysctl net.ipv4.ip_forward=1")

    r4.cmd("route add -net 192.168.0.0/24 gw 192.168.5.2")
    r4.cmd("route add -net 192.168.1.0/24 gw 192.168.7.1")
    r4.cmd("route add -net 192.168.2.0/24 gw 192.168.7.1")
    r4.cmd("route add -net 192.168.2.0/24 gw 192.168.5.2")
    r4.cmd("route add -net 192.168.6.0/24 gw 192.168.7.1")
    r4.cmd("route add -net 192.168.4.0/24 gw 192.168.5.2")
    
    #membuat trafic iperf server client dalam background
    h2.cmdPrint("iperf -s &")     
    h1.cmdPrint("iperf -t 60 -B 192.162.0.2 -c 192.168.2.2 &")
    #h1.cmdPrint("iperf -t 60 -B 192.162.1.2 -c 192.168.2.2 &")


    CLI(net)
    net.stop()

a = 0
while(a != '1'and a != '2'and a != '3' ):
    print('Selamat Datang Di Tubes Jarkom')
    print('1. Masuk ke CLO 1')
    print('2. Masuk ke CLO 2 dan 3')
    print('3. Masuk ke CLO 4')
    a = input('Pilih : ')

if(a=='1'):
    setLogLevel('info')
    clo1()
elif(a=='2'):
    setLogLevel('info')
    clo2_3()
elif(a=='3'):
    buffer = -1
    while( buffer != '20' and buffer != '40' and buffer != '60' and buffer != '100'):
        buffer = input('Masukan Nilai Buffer (20/40/60/100) : ')
    setLogLevel('info')
    clo4(buffer)
