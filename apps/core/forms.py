
from django import forms
from django.core.exceptions import ValidationError
import ipaddress
from django.utils import ipv6


class SubnetForm(forms.Form):
    ip_address = forms.CharField(label='Enter an IP address', max_length=15)
    subnet_mask = forms.CharField(label='Enter a subnet mask', max_length=15)

    def clean_ip_address(self):
        ip_address = self.cleaned_data['ip_address']
        ip_octets = ip_address.split('.')
        if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (
                int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (
                0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
            return ip_address
        else:
            raise ValidationError("The IP address is INVALID! Please retry")

    def clean_subnet_mask(self):
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
        subnet_mask = self.cleaned_data['subnet_mask']
        mask_octets = subnet_mask.split('.')
        if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (
                int(mask_octets[2]) in masks) and (int(mask_octets[3]) in masks) and (
                int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
            return subnet_mask
        else:
            raise ValidationError("The IP address is INVALID! Please retry")

    def calculate_subnet(self):

        ip_octets = self.cleaned_data['ip_address'].split('.')
        mask_octets = self.cleaned_data['subnet_mask'].split('.')

        mask_octets_binary = []

        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            # print(binary_octet)

            mask_octets_binary.append(binary_octet.zfill(8))

        # print(mask_octets_binary)

        binary_mask = "".join(mask_octets_binary)
        # print(decimal_mask)
        # Example: for 255.255.255.0 => 11111111111111111111111100000000

        # Counting host bits in the mask and calculating number of hosts/subnet
        no_of_zeros = binary_mask.count("0")
        no_of_ones = 32 - no_of_zeros
        no_of_hosts = abs(2 ** no_of_zeros - 2)  # return a positive value for the /32 mask (all 255s)

        # print(no_of_zeros)
        # print(no_of_ones)
        # print(no_of_hosts)

        # Obtaining wildcard mask
        wildcard_octets = []

        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))

        # print(wildcard_octets)

        wildcard_mask = ".".join(wildcard_octets)
        # print(wildcard_mask)

        # Application #1 - Part #3

        # Convert IP to binary string
        ip_octets_binary = []

        for octet in ip_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            # print(binary_octet)

            ip_octets_binary.append(binary_octet.zfill(8))

        # print(ip_octets_binary)
        # Example: for 192.168.10.1 =>

        binary_ip = "".join(ip_octets_binary)

        # print(binary_ip)
        # Example: for 192.168.2.100 => 11000000101010000000101000000001

        # Getting the network address and broadcast address from the binary strings obtained above

        network_address_binary = binary_ip[:(no_of_ones)] + "0" * no_of_zeros
        # print(network_address_binary)

        broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
        # print(broadcast_address_binary)

        # Converting everything back to decimal (readable format)
        net_ip_octets = []

        # range(0, 32, 8) means 0, 8, 16, 24
        for bit in range(0, 32, 8):
            net_ip_octet = network_address_binary[bit: bit + 8]
            net_ip_octets.append(net_ip_octet)

        # We will end up with 4 slices of the binary IP address: [0: 8], [8: 16], [16: 24] and [24:31]; remember that each slice goes up to, but not including, the index on the right side of the colon!

        # print(net_ip_octets)

        net_ip_address = []

        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))

        # print(net_ip_address)

        network_address = ".".join(net_ip_address)
        # print(network_address)

        bst_ip_octets = []

        # range(0, 32, 8) means 0, 8, 16, 24
        for bit in range(0, 32, 8):
            bst_ip_octet = broadcast_address_binary[bit: bit + 8]
            bst_ip_octets.append(bst_ip_octet)

        # print(bst_ip_octets)

        bst_ip_address = []

        for each_octet in bst_ip_octets:
            bst_ip_address.append(str(int(each_octet, 2)))

        # print(bst_ip_address)

        broadcast_address = ".".join(bst_ip_address)
        # print(broadcast_address)

        print(
            {
                'network_address': network_address,
                'broadcast_address': broadcast_address,
                'no_of_hosts': no_of_hosts,
                'wildcard_mask': wildcard_mask,
                'mask_bits': no_of_ones,
            }
        )
        # Results for selected IP/mask
        return {
            'network_address': network_address,
            'broadcast_address': broadcast_address,
            'no_of_hosts': no_of_hosts,
            'wildcard_mask': wildcard_mask,
            'mask_bits': no_of_ones,
        }


class ConvertForm(forms.Form):
    ip_address = forms.CharField(label='Enter an IP address', max_length=15)

    def clean_ip_address(self):
        ip_address = self.cleaned_data['ip_address']
        ip_octets = ip_address.split('.')
        if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223)  and (
                int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (
                0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
            return ip_address
        else:
            raise ValidationError("The IP address is INVALID! Please retry")

    def convert_dec_to_bin(self):

        ip_octets = self.cleaned_data['ip_address'].split('.')
        print("IP in binary is")

        binary_ip = (
            '{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(
                int(ip_octets[0]),
                int(ip_octets[1]),
                int(ip_octets[2]),
                int(ip_octets[3])
            )
        )

        return {
            'binary_IP': binary_ip,
        }


class ValidIPv6Form(forms.Form):
    ip_address = forms.CharField(label='Enter an IP address', max_length=39)

    def valid_ipv6(self):
        ip_address = self.cleaned_data['ip_address']
        addr = None
        ip = None
        try:
            ip = ipaddress.IPv6Address(ip_address)

            if ip.is_multicast:
                addr = 'an IPv6 multicast address'
            if ip.is_private:
                addr = 'an IPv6 private address'
            if ip.is_global:
                addr = 'an IPv6 global address'
            if ip.is_link_local:
                addr = 'an IPv6 link-local address'
            if ip.is_site_local:
                addr = 'an IPv6 site-local address'
            if ip.is_reserved:
                addr = 'an IPv6 reserved address'
            if ip.is_loopback:
                addr = 'an IPv6 loopback address'
            if ip.ipv4_mapped:
                addr = 'an IPv6 mapped IPv4 address'
            if ip.sixtofour:
                addr = 'an IPv6 RFC 3056 address'
            if ip.teredo:
                addr = 'an IPv6 RFC 4380 address'

        except ipaddress.AddressValueError:
            addr = 'not a valid IPv6 address'

        return {
            'ip': ip,
            'addr': addr
        }


class ExpandForm(forms.Form):
    ip_address = forms.CharField(label='Enter the IP to be expanded', max_length=39)
    # Ipv6 address expander

    def expand_ipv6(self):
        ip_address = self.cleaned_data['ip_address']

        try:
            ip = ipaddress.IPv6Address(ip_address)
            addr = ipaddress.ip_address(ip)

            return {
                'ip': ip_address,
                'expand_addr': addr.exploded,
            }

        except ipaddress.AddressValueError:
            return {
                'ip': ip_address,
                'error': ' It is not a valid IPv6 address',

            }
