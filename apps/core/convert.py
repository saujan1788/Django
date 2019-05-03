from django import forms
from django.core.exceptions import ValidationError


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

    def covert_dec_to_bin(self):

        ip_octets = self.cleaned_data['ip_address'].split('.')
        print("IP in binary is")

        binary_IP = ('{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ip_octets[0]),int(ip_octets[1]),int(ip_octets[2]),int(ip_octets[3]))

        print(
        {
            'binary_IP': binary_IP,
        }
        )
        return {
            'binary_IP': binary_IP,
        }
