[![PyPI](https://img.shields.io/pypi/v/napalm-fortios.svg)](https://pypi.python.org/pypi/napalm-fortios)
[![PyPI](https://img.shields.io/pypi/dm/napalm-fortios.svg)](https://pypi.python.org/pypi/napalm-fortios)
[![Build Status](https://travis-ci.org/napalm-automation/napalm-fortios.svg?branch=master)](https://travis-ci.org/napalm-automation/napalm-fortios)
[![Coverage Status](https://coveralls.io/repos/github/napalm-automation/napalm-fortios/badge.svg?branch=master)](https://coveralls.io/github/napalm-automation/napalm-fortios)


# napalm-fortios

[NAPALM](https://napalm-automation.net/) driver for Fortinet FortiOS networking
equipment.

## Supported devices

Fortinet FortiOS devices should be supported.

Open an issue on GitHub if you find any problems.

## Supported Getters

| Getter                    | Support  |
|---------------------------|----------|
| get_arp_table             |  ✅      |
| get_bgp_config            |  ❌      |
| get_bgp_neighbors         |  ✅      |
| get_bgp_neighbors_detail  |  ❌      |
| get_config                |  ✅      |
| get_environment           |  ✅      |
| get_facts                 |  ✅      |
| get_firewall_policies     |  ✅      |
| get_interfaces            |  ✅      |
| get_interfaces_counters   |  ✅      |
| get_interfaces_ip         |  ✅      |
| get_ipv6_neighbors_table  |  ❌      |
| get_lldp_neighbors        |  ❌      |
| get_lldp_neighbors_detail |  ❌      |
| get_mac_address_table     |  ❌      |
| get_network_instances     |  ❌      |
| get_ntp_peers             |  ❌      |
| get_ntp_servers           |  ❌      |
| get_ntp_stats             |  ❌      |
| get_optics                |  ❌      |
| get_probes_config         |  ❌      |
| get_probes_results        |  ❌      |
| get_route_to              |  ❌      |
| get_snmp_information      |  ❌      |
| get_users                 |  ❌      |
| is_alive                  |  ✅      |
| ping                      |  ❌      |
| traceroute                |  ❌      |

## Usage

Install napalm and napalm-fortios via pip:
```
$ pip install napalm napalm-fortios
```

Test functionality:
```
#!/usr/bin/env python3
# Simple napalm-fortios test

from napalm import get_network_driver

driver = get_network_driver("fortios")

device = driver(
    "1.2.3.4",
    "admin",
    "password",
    optional_args={"port": 22},
)

device.open()

facts = device.get_facts()

device.close()

print(facts)
```

See the full [NAPALM Docs](https://napalm.readthedocs.io/en/latest/index.html) for more detailed instructions.

## License

Apache License, Version 2.0
