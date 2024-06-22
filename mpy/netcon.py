import network
def connect(wifi,pwd):
    sta_if = network.WLAN(network.STA_IF);sta_if.active(False);sta_if.active(True)
    print(sta_if.scan())                             # Scan for available access points
    sta_if.connect(wifi,pwd) # Connect to an AP
    # sta_if.connect("OnePlus 8 Pro", "n6ggk5gs") # Connect to an AP
    print(sta_if.ifconfig())

