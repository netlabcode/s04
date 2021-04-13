#Topology Substation 4-14-27
#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Node, Controller, RemoteController, OVSSwitch, OVSKernelSwitch, Host
from mininet.cli import CLI
from mininet.link import Intf, TCLink
from mininet.log import setLogLevel, info
from mininet.node import Node, CPULimitedHost
from mininet.util import irange,dumpNodeConnections
import time
import os



class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()

def emptyNet():

    NODE2_IP='192.168.56.1'
    CONTROLLER_IP='127.0.0.1'

    net = Mininet( topo=None,
                   build=False)

    #c0 = net.addController( 'c0',controller=RemoteController,ip=CONTROLLER_IP,port=6633)
    net.addController('c0', port=6633)

    r0 = net.addHost('r0', cls=LinuxRouter, ip='100.0.0.1/16')
    r4 = net.addHost('r4', cls=LinuxRouter, ip='100.4.0.1/16')
    r14 = net.addHost('r14', cls=LinuxRouter, ip='100.14.0.1/16')
    r27 = net.addHost('r27', cls=LinuxRouter, ip='100.27.0.1/16')


    #Switch External Gateway
    s777 = net.addSwitch( 's777' )

    #Switch on Control Center
    s999 = net.addSwitch( 's999' )

    #Switch on Substation
    s41 = net.addSwitch( 's41' )
    s42 = net.addSwitch( 's42' )
    s43 = net.addSwitch( 's43' )
    s141 = net.addSwitch( 's141' )
    s142 = net.addSwitch( 's142' )
    s143 = net.addSwitch( 's143' )
    s271 = net.addSwitch( 's271' )
    s272 = net.addSwitch( 's272' )
    s273 = net.addSwitch( 's273' )

    # Add host-switch links in the same subnet
    net.addLink(s999, r0, intfName2='r0-eth1', params2={'ip': '100.0.0.1/16'})
    net.addLink(s41, r4, intfName2='r4-eth1', params2={'ip': '100.4.0.1/16'})
    net.addLink(s141, r14, intfName2='r14-eth1', params2={'ip': '100.14.0.1/16'})
    net.addLink(s271, r27, intfName2='r27-eth1', params2={'ip': '100.27.0.1/16'})

     # Add router-router link in a new subnet for the router-router connection
    net.addLink(r0, r4, intfName1='r0-eth3', intfName2='r4-eth2', params1={'ip': '200.4.0.1/24'}, params2={'ip': '200.4.0.2/24'})
    net.addLink(r0, r14, intfName1='r0-eth2', intfName2='r14-eth2', params1={'ip': '200.14.0.1/24'}, params2={'ip': '200.14.0.2/24'})
    net.addLink(r0, r27, intfName1='r0-eth4', intfName2='r27-eth2', params1={'ip': '200.27.0.1/24'}, params2={'ip': '200.27.0.2/24'})

    #Add Host on Control Center
    ccdb = net.addHost('ccdb', ip='100.0.0.11')
    cctl = net.addHost('cctl', ip='100.0.0.12')

    #Add Hosts on Substation 4
    s04m1 = net.addHost('s04m1', ip='100.4.0.11', cls=CPULimitedHost, cpu=.1)
    s04m2 = net.addHost('s04m2', ip='100.4.0.12', cls=CPULimitedHost, cpu=.1)
    s04m3 = net.addHost('s04m3', ip='100.4.0.13', cls=CPULimitedHost, cpu=.1)
    s04m4 = net.addHost('s04m4', ip='100.4.0.14', cls=CPULimitedHost, cpu=.1)
    s04m5 = net.addHost('s04m5', ip='100.4.0.15', cls=CPULimitedHost, cpu=.1)
    s04m6 = net.addHost('s04m6', ip='100.4.0.16', cls=CPULimitedHost, cpu=.1)
    s04m7 = net.addHost('s04m7', ip='100.4.0.17', cls=CPULimitedHost, cpu=.1)
    s04m8 = net.addHost('s04m8', ip='100.4.0.18', cls=CPULimitedHost, cpu=.1)
    s04m9 = net.addHost('s04m9', ip='100.4.0.19', cls=CPULimitedHost, cpu=.1)
    s04cpc = net.addHost('s04cpc', ip='100.4.0.21')
    s04db = net.addHost('s04db', ip='100.4.0.22')
    s04gw = net.addHost('s04gw', ip='100.4.0.23')

    #Add Hosts on Substation 14
    s14m1 = net.addHost('s14m1', ip='100.14.0.11', cls=CPULimitedHost, cpu=.1)
    s14m2 = net.addHost('s14m2', ip='100.14.0.12', cls=CPULimitedHost, cpu=.1)
    s14m3 = net.addHost('s14m3', ip='100.14.0.13', cls=CPULimitedHost, cpu=.1)
    s14m4 = net.addHost('s14m4', ip='100.14.0.14', cls=CPULimitedHost, cpu=.1)
    s14m5 = net.addHost('s14m5', ip='100.14.0.15', cls=CPULimitedHost, cpu=.1)
    s14m6 = net.addHost('s14m6', ip='100.14.0.16', cls=CPULimitedHost, cpu=.1)
    s14cpc = net.addHost('s14cpc', ip='100.14.0.21')
    s14db = net.addHost('s14db', ip='100.14.0.22')
    s14gw = net.addHost('s14gw', ip='100.14.0.23')

    #Add Hosts on Substation 17
    s27m1 = net.addHost('s27m1', ip='100.27.0.11', cls=CPULimitedHost, cpu=.1)
    s27m2 = net.addHost('s27m2', ip='100.27.0.12', cls=CPULimitedHost, cpu=.1)
    s27m3 = net.addHost('s27m3', ip='100.27.0.13', cls=CPULimitedHost, cpu=.1)
    s27m4 = net.addHost('s27m4', ip='100.27.0.14', cls=CPULimitedHost, cpu=.1)
    s27m5 = net.addHost('s27m5', ip='100.27.0.15', cls=CPULimitedHost, cpu=.1)
    s27m6 = net.addHost('s27m6', ip='100.27.0.16', cls=CPULimitedHost, cpu=.1)
    s27cpc = net.addHost('s27cpc', ip='100.27.0.21')
    s27db = net.addHost('s27db', ip='100.27.0.22')
    s27gw = net.addHost('s27gw', ip='100.27.0.23')

    # Link siwtch to switch
    net.addLink(s41,s42)
    net.addLink(s43,s42)
    net.addLink(s141,s142)
    net.addLink(s143,s142)
    net.addLink(s271,s272)
    net.addLink(s273,s272)

    # Link Control Center to Switch
    net.addLink(ccdb,s999, intfName1='ccdb-eth1', params1={'ip':'100.0.0.11/24'})
    net.addLink(cctl,s999, intfName1='cctl-eth1', params1={'ip':'100.0.0.12/24'})

    # Link Substation 04 Merging unit to Switch
    net.addLink(s04m1,s43, intfName1='s04m1-eth1', params1={'ip':'100.4.0.11/24'})
    net.addLink(s04m2,s43, intfName1='s04m2-eth1', params1={'ip':'100.4.0.12/24'})
    net.addLink(s04m3,s43, intfName1='s04m3-eth1', params1={'ip':'100.4.0.13/24'})
    net.addLink(s04m4,s43, intfName1='s04m4-eth1', params1={'ip':'100.4.0.14/24'})
    net.addLink(s04m5,s43, intfName1='s04m5-eth1', params1={'ip':'100.4.0.15/24'})
    net.addLink(s04m6,s43, intfName1='s04m6-eth1', params1={'ip':'100.4.0.16/24'})
    net.addLink(s04m7,s43, intfName1='s04m7-eth1', params1={'ip':'100.4.0.17/24'})
    net.addLink(s04m8,s43, intfName1='s04m8-eth1', params1={'ip':'100.4.0.14/24'})
    net.addLink(s04m9,s43, intfName1='s04m9-eth1', params1={'ip':'100.4.0.19/24'})  
    net.addLink(s04cpc,s42)
    net.addLink(s04db,s42)
    net.addLink(s04gw,s41, intfName1='s04gw-eth1', params1={'ip':'100.4.0.23/24'})
    
    # Link Substation 14 Merging unit to Switch
    net.addLink(s14m1,s143, intfName1='s14m1-eth1', params1={'ip':'100.14.0.11/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s14m2,s143, intfName1='s14m2-eth1', params1={'ip':'100.14.0.12/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s14m3,s143, intfName1='s14m3-eth1', params1={'ip':'100.14.0.13/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s14m4,s143, intfName1='s14m4-eth1', params1={'ip':'100.14.0.14/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s14m5,s143, intfName1='s14m5-eth1', params1={'ip':'100.14.0.15/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s14m6,s143, intfName1='s14m6-eth1', params1={'ip':'100.14.0.16/24'}, cls=TCLink, bw=0.01 )
    net.addLink(s14cpc,s142)
    net.addLink(s14db,s142)
    net.addLink(s14gw,s141, intfName1='s14gw-eth1', params1={'ip':'100.14.0.23/24'})

    # Link Substation 27 Merging unit to Switch
    net.addLink(s27m1,s273, intfName1='s27m1-eth1', params1={'ip':'100.27.0.11/24'})
    net.addLink(s27m2,s273, intfName1='s27m2-eth1', params1={'ip':'100.27.0.12/24'})
    net.addLink(s27m3,s273, intfName1='s27m3-eth1', params1={'ip':'100.27.0.13/24'})
    net.addLink(s27m4,s273, intfName1='s27m4-eth1', params1={'ip':'100.27.0.14/24'})
    net.addLink(s27m5,s273, intfName1='s27m5-eth1', params1={'ip':'100.27.0.15/24'})
    net.addLink(s27m6,s273, intfName1='s27m6-eth1', params1={'ip':'100.27.0.16/24'}) 
    net.addLink(s27cpc,s272)
    net.addLink(s27db,s272)
    net.addLink(s27gw,s271, intfName1='s27gw-eth1', params1={'ip':'100.27.0.23/24'})


    # Link Host Control Center to External gateway
    net.addLink(ccdb,s777, intfName1='ccdb-eth0', params1={'ip':'10.0.0.11/16'})
    net.addLink(cctl,s777, intfName1='cctl-eth0', params1={'ip':'10.0.0.12/16'})

    # Link Host Substation 13 to switch to external gateway
    net.addLink(s04m1,s777, intfName1='s04m1-eth0', params1={'ip':'10.0.4.11/16'})
    net.addLink(s04m2,s777, intfName1='s04m2-eth0', params1={'ip':'10.0.4.12/16'})
    net.addLink(s04m3,s777, intfName1='s04m3-eth0', params1={'ip':'10.0.4.13/16'})
    net.addLink(s04m4,s777, intfName1='s04m4-eth0', params1={'ip':'10.0.4.14/16'})
    net.addLink(s04m5,s777, intfName1='s04m5-eth0', params1={'ip':'10.0.4.15/16'})
    net.addLink(s04m6,s777, intfName1='s04m6-eth0', params1={'ip':'10.0.4.16/16'})
    net.addLink(s04m7,s777, intfName1='s04m7-eth0', params1={'ip':'10.0.4.17/16'})
    net.addLink(s04m8,s777, intfName1='s04m8-eth0', params1={'ip':'10.0.4.18/16'})
    net.addLink(s04m9,s777, intfName1='s04m9-eth0', params1={'ip':'10.0.4.19/16'})
    net.addLink(s04gw,s777, intfName1='s04gw-eth0', params1={'ip':'10.0.4.23/16'})
    
    # Link Host Substation 10 to switch to external gateway
    net.addLink(s14m1,s777, intfName1='s14m1-eth0', params1={'ip':'10.0.14.11/16'})
    net.addLink(s14m2,s777, intfName1='s14m2-eth0', params1={'ip':'10.0.14.12/16'})
    net.addLink(s14m3,s777, intfName1='s14m3-eth0', params1={'ip':'10.0.14.13/16'})
    net.addLink(s14m4,s777, intfName1='s14m4-eth0', params1={'ip':'10.0.14.14/16'})
    net.addLink(s14m5,s777, intfName1='s14m5-eth0', params1={'ip':'10.0.14.15/16'})
    net.addLink(s14m6,s777, intfName1='s14m6-eth0', params1={'ip':'10.0.14.16/16'})
    net.addLink(s14gw,s777, intfName1='s14gw-eth0', params1={'ip':'10.0.14.23/16'})

    # Link Host Substation 27 to switch to external gateway
    net.addLink(s27m1,s777, intfName1='s27m1-eth0', params1={'ip':'10.0.27.11/16'})
    net.addLink(s27m2,s777, intfName1='s27m2-eth0', params1={'ip':'10.0.27.12/16'})
    net.addLink(s27m3,s777, intfName1='s27m3-eth0', params1={'ip':'10.0.27.13/16'})
    net.addLink(s27m4,s777, intfName1='s27m4-eth0', params1={'ip':'10.0.27.14/16'})
    net.addLink(s27m5,s777, intfName1='s27m5-eth0', params1={'ip':'10.0.27.15/16'})
    net.addLink(s27m6,s777, intfName1='s27m6-eth0', params1={'ip':'10.0.27.16/16'})
    net.addLink(s27gw,s777, intfName1='s27gw-eth0', params1={'ip':'10.0.27.23/16'})

    


    #Build and start Network ============================================================================
    net.build()
    net.addNAT(ip='10.0.0.250').configDefault()
    net.start()

    #Configure GRE Tunnel
    #s777.cmdPrint('ovs-vsctl add-port s777 s777-gre1 -- set interface s777-gre1 type=gre ofport_request=5 options:remote_ip='+NODE2_IP)
    #s777.cmdPrint('ovs-vsctl show')
    nat = net.get('nat0')
    nat.cmdPrint('ip link set mtu 1454 dev nat0-eth0')

    # Add routing for reaching networks that aren't directly connected
    info( net[ 'r0' ].cmd( 'ip route add 100.4.0.0/24 via 200.4.0.2 dev r0-eth3' ) )
    info( net[ 'r4' ].cmd( 'ip route add 100.0.0.0/24 via 200.4.0.1 dev r4-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.14.0.0/24 via 200.14.0.2 dev r0-eth2' ) )
    info( net[ 'r14' ].cmd( 'ip route add 100.0.0.0/24 via 200.14.0.1 dev r14-eth2' ) )

    info( net[ 'r0' ].cmd( 'ip route add 100.27.0.0/24 via 200.27.0.2 dev r0-eth4' ) )
    info( net[ 'r27' ].cmd( 'ip route add 100.0.0.0/24 via 200.27.0.1 dev r27-eth2' ) )

    info( net[ 's04m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.4.0.1 dev s04m1-eth1' ) )
    info( net[ 's04m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.4.0.1 dev s04m2-eth1' ) )
    info( net[ 's04m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.4.0.1 dev s04m3-eth1' ) )
    info( net[ 's04m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.4.0.1 dev s04m4-eth1' ) )
    info( net[ 's04m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.4.0.1 dev s04m5-eth1' ) )
    info( net[ 's04m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.4.0.1 dev s04m6-eth1' ) )
    info( net[ 's04m7' ].cmd( 'ip route add 100.0.0.0/24 via 100.4.0.1 dev s04m7-eth1' ) )
    info( net[ 's04m8' ].cmd( 'ip route add 100.0.0.0/24 via 100.4.0.1 dev s04m8-eth1' ) )
    info( net[ 's04m9' ].cmd( 'ip route add 100.0.0.0/24 via 100.4.0.1 dev s04m9-eth1' ) )

    info( net[ 's14m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.14.0.1 dev s14m1-eth1' ) )
    info( net[ 's14m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.14.0.1 dev s14m2-eth1' ) )
    info( net[ 's14m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.14.0.1 dev s14m3-eth1' ) )
    info( net[ 's14m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.14.0.1 dev s14m4-eth1' ) )
    info( net[ 's14m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.14.0.1 dev s14m5-eth1' ) )
    info( net[ 's14m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.14.0.1 dev s14m6-eth1' ) )

    info( net[ 's27m1' ].cmd( 'ip route add 100.0.0.0/24 via 100.27.0.1 dev s27m1-eth1' ) )
    info( net[ 's27m2' ].cmd( 'ip route add 100.0.0.0/24 via 100.27.0.1 dev s27m2-eth1' ) )
    info( net[ 's27m3' ].cmd( 'ip route add 100.0.0.0/24 via 100.27.0.1 dev s27m3-eth1' ) )
    info( net[ 's27m4' ].cmd( 'ip route add 100.0.0.0/24 via 100.27.0.1 dev s27m4-eth1' ) )
    info( net[ 's27m5' ].cmd( 'ip route add 100.0.0.0/24 via 100.27.0.1 dev s27m5-eth1' ) )
    info( net[ 's27m6' ].cmd( 'ip route add 100.0.0.0/24 via 100.27.0.1 dev s27m6-eth1' ) )
    
    info( net[ 'ccdb' ].cmd( 'ip route add 100.4.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.14.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )
    info( net[ 'ccdb' ].cmd( 'ip route add 100.27.0.0/24 via 100.0.0.1 dev ccdb-eth1' ) )

    info( net[ 'cctl' ].cmd( 'ip route add 100.4.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.14.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    info( net[ 'cctl' ].cmd( 'ip route add 100.27.0.0/24 via 100.0.0.1 dev cctl-eth1' ) )
    
    info(os.system('ip addr add 100.0.0.99/24 dev s999'))
    info(os.system('ip link set s999 up'))

    """

    time.sleep(2)

    info( net[ 's04m1' ].cmd( 'python3 as04m1.py &amp' ) )
    info( net[ 's04m2' ].cmd( 'python3 as04m2.py &amp' ) )
    info( net[ 's04m3' ].cmd( 'python3 as04m3.py &amp' ) )
    info( net[ 's04m4' ].cmd( 'python3 as04m4.py &amp' ) )
    info( net[ 's04m5' ].cmd( 'python3 as04m5.py &amp' ) )
    info( net[ 's04m6' ].cmd( 'python3 as04m6.py &amp' ) )

    info( net[ 's14m1' ].cmd( 'python3 as14m1.py &amp' ) )
    info( net[ 's14m2' ].cmd( 'python3 as14m2.py &amp' ) )
    info( net[ 's14m3' ].cmd( 'python3 as14m3.py &amp' ) )

    info( net[ 's27m1' ].cmd( 'python3 as27m1.py &amp' ) )
    info( net[ 's27m2' ].cmd( 'python3 as27m2.py &amp' ) )
    info( net[ 's27m3' ].cmd( 'python3 as27m3.py &amp' ) )

    time.sleep(2)

    info( net[ 's04gw' ].cmd( 'python3 as04gdb.py &amp' ) )
    info( net[ 's14gw' ].cmd( 'python3 as14gdb.py &amp' ) )
    info( net[ 's27gw' ].cmd( 'python3 as27gdb.py &amp' ) )

    time.sleep(2)

    info( net[ 's04gw' ].cmd( 'python3 as04gcc.py &amp' ) )
    info( net[ 's14gw' ].cmd( 'python3 as14gcc.py &amp' ) )
    info( net[ 's27gw' ].cmd( 'python3 as27gcc.py &amp' ) )

    """


    CLI( net )
    net.stop()



if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()