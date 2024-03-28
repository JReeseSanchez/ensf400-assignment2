from ansible_runner import Runner

def load_inventory():
    # Create Runner object
    r = Runner(
        playbook='ping.yml',
        inventory='inventory.ini'
    )

    # Run playbook
    r.run()

    # Get host information
    for host in r.inventory.hosts:
        print("Host: {}".format(host))
        print("  IP Address: {}".format(r.inventory.get_host(host).vars['ansible_host']))
        print("  Groups: {}".format(', '.join(r.inventory.get_host(host).groups)))

if __name__ == "__main__":
    load_inventory()
