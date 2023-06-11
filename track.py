import os,sys
import requests

YOUR_API_KEY = '267e01c12ad64578858f6317223da22c'

def get_ip_details(ip_address):
    url = f'https://api.ipgeolocation.io/ipgeo?apiKey={YOUR_API_KEY}&ip={ip_address}'

    try:
        response = requests.get(url)
        data = response.json()

        if 'ip' in data:
            print('\n\nLayanan Perusahaan: ', data['organization'])
            print('Alamat IP:', data['ip'])
            print('Jenis Koneksi: ', data['connection_type'])
            print('Negara:', data['country_name'])
            print('Kota:', data['city'])
            print('Kode Pos:', data['zipcode'])
            print('Koordinat:', data['latitude'], data['longitude'])
        else:
            print('Gagal mendapatkan detail IP')

    except requests.exceptions.RequestException as e:
        print('Terjadi kesalahan saat melakukan permintaan:', str(e))


os.system('clear')
print('#################################')
print('Buitenzorg Track Location from IP\n    Author By Prakasa_Jr644')
print('#################################\n')
ip = input('Masukkan alamat IP: ')
get_ip_details(ip)
