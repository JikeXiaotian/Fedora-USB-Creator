import os

wget_arguments = "-P " + os.getcwd()


def download_iso():
    fedora_iso_link = "https://download.fedoraproject.org/pub/fedora/linux/releases/31/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-31-1.9.iso "
    os.system("wget " + fedora_iso_link + wget_arguments)

def verify_checksum():
    os.system("curl https://getfedora.org/static/fedora.gpg | gpg --import")    # Import the GPG key of Fedora
    iso_checksum_link = "https://getfedora.org/static/checksums/Fedora-Workstation-31-1.9-x86_64-CHECKSUM "
    os.system("wget " + iso_checksum_link + wget_arguments)
    os.system("gpg --verify-files *-CHECKSUM")
    os.system("sha256sum -c *-CHECKSUM")

def choose_drive():
    print("")
    print("Please choose the disk you want to burn Fedora into: ")
    os.system("ls /dev/ | grep sd")
    choice = input("Tell me your dicision: ")
    return choice

def confirm(target_drive):
    print("Are you sure that you want to burn Fedora iso into /dev/" + target_drive + "? All the data in the drive will be removed and there will be no choice going back!")
    if input("Your answer(y/n): ") == 'y':
        return 0
    else:
        return -1


def burn(target_drive):
    print("sudo dd if=" + os.getcwd() + "/Fedora-Workstation-Live-x86_64-31-1.9.iso" + " of=/dev/" + target_drive + " bs=4M") 

def main():
    download_iso()
    verify_checksum()
    target_drive = choose_drive()
    if confirm(target_drive) == -1:
        print("Cancelled.")
        return
    burn(target_drive)

main()
