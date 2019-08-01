#!/usr/bin/env python3
def check_drive_type():
    blocks = ['sdb', 'sdc']
    for block in blocks:
        try:
            with open('/sys/block/{}/queue/rotational'.format(block), 'r') as cid:
                return cid.read().split()[0]
        except FileNotFoundError:
            continue
    return -1


if __name__ == '__main__':
    drive_type = check_drive_type()
    if drive_type == -1:
        print("ERROR: The script couldn't determine the disk type. "
              "The rotational files could not be found.")
    elif drive_type == "0":
        print('Drive: SSD')
    else:
        print('Drive: SATA')
