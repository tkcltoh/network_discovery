import argparse
import nmap
import pandas as pd


def main():
    try:

        parser = argparse.ArgumentParser(description='Read in network address')
        parser.add_argument('-n',dest='netaddr', type=str, required=True, help='Enter CIDR address ie 192.168.0.0/24, max value = 2. Use space to separate network')

        args = parser.parse_args()

        output = r'inventory.csv'
        column_name = ['Host', 'Status']

        nm = nmap.PortScanner()
        print('Discover host in {}'.format(args.netaddr))
        nm.scan(hosts=args.netaddr,arguments='-sn')
        for host in nm.all_hosts():
            with open('inv.txt','a') as f:
                f.write('%s ,' % (host))
                f.write('%s \n' % nm[host].state())

                df = pd.read_csv("inv.txt", delimiter=',', names=column_name)
                df.to_csv('inventory.csv')

    except Exception as message:
        print(type(message))




if __name__ == '__main__':
    main()


