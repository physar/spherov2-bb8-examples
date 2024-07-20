# Created by Arnoud Visser, by combyning several examples
# credit to two sources ...
# https://github.com/hbldh/bleak/blob/55a2d34cc96bb842be278485794806704caa2d2c/examples/scanner_byname.py
# https://github.com/hbldh/bleak/blob/develop/examples/sensortag.py

import asyncio
from bleak import BleakScanner, BleakClient
from bleak.uuids import normalize_uuid_16, uuid16_dict

MODEL_NBR_UUID = "2A24"

GENERIC_GATT_SERIAL_NUMBER_STRING_UUID = "00002a25-0000-1000-8000-00805f9b34fb"

uuid16_lookup = {v: normalize_uuid_16(k) for k, v in uuid16_dict.items()}

DEVICE_NAME_UUID = uuid16_lookup["Device Name"]

async def scan():
    return await BleakScanner.find_device_by_filter(
        lambda d, ad: d.name and d.name.startswith("BB-8") 
    )

async def connect(device):
    async with BleakClient(device) as client:
        print("Connected with a BB-8 via bluetooth")

        try:
            device_name = await client.read_gatt_char(DEVICE_NAME_UUID)
            print("Device Full Name: {0}".format("".join(map(chr, device_name))))
        except Exception:
            print("Looking up full name failed")
            pass

        try:
            serial_number = await client.read_gatt_char(GENERIC_GATT_SERIAL_NUMBER_STRING_UUID)
            print("Serial number: {0}".format("".join(map(chr, serial_number))))
        except Exception:
            print("Looking up serial number failed")
            pass


# Do have one async main function that does everything.
async def main():
    device = await scan()
    if not device:
        print("Device not found")
        return

    await connect(device)

asyncio.run(main())
