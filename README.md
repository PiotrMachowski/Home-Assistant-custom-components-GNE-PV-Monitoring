[![HACS Custom][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Ko-Fi][ko_fi_shield]][ko_fi]
[![PayPal.Me][paypal_me_shield]][paypal_me]


[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Custom&style=popout&color=orange&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white
[hacs]: https://hacs.xyz/docs/default_repositories

[latest_release]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-GNE-PV-Monitoring/releases/latest
[releases_shield]: https://img.shields.io/github/release/PiotrMachowski/Home-Assistant-custom-components-GNE-PV-Monitoring.svg?style=popout

[releases]: https://github.com/PiotrMachowski/Home-Assistant-custom-components-GNE-PV-Monitoring/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/PiotrMachowski/Home-Assistant-custom-components-GNE-PV-Monitoring/total

[ko_fi_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Ko-Fi&color=F16061&logo=ko-fi&logoColor=white
[ko_fi]: https://ko-fi.com/piotrmachowski

[buy_me_a_coffee_shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy_me_a_coffee]: https://www.buymeacoffee.com/PiotrMachowski

[paypal_me_shield]: https://img.shields.io/static/v1.svg?label=%20&message=PayPal.Me&logo=paypal
[paypal_me]: https://paypal.me/PiMachowski


# GNE Photovoltaic Monitoring

This sensor uses official API to get data from GNE.

## Configuration

To configure this integration go to: _Configuration_ -> _Integrations_ -> _Add integration_ -> _GNE PV Monitoring_.

You can also use following [My Home Assistant](http://my.home-assistant.io/) link

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=gne_pv_monitoring)

## Installation

### Using [HACS](https://hacs.xyz/) (recommended)

* In _Integrations_ section add this repository `https://github.com/PiotrMachowski/Home-Assistant-custom-components-GNE-PV-Monitoring` with type `integration`
* Install added repository
 
### Manual

Download [*gne_pv_monitoring.zip*](https://github.com/PiotrMachowski/Home-Assistant-custom-components-GNE-PV-Monitoring/releases/latest/download/gne_pv_monitoring.zip) and extract its contents to `config/custom_components/gne_pv_monitoring` directory:
```bash
mkdir -p custom_components/gne_pv_monitoring
cd custom_components/gne_pv_monitoring
wget https://github.com/PiotrMachowski/Home-Assistant-custom-components-GNE-PV-Monitoring/releases/latest/download/gne_pv_monitoring.zip
unzip gne_pv_monitoring.zip
rm gne_pv_monitoring.zip
```

Finally, restart Home Assistant and configure the integration.

<a href='https://ko-fi.com/piotrmachowski' target='_blank'><img height='35' style='border:0px;height:46px;' src='https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' />
<a href="https://paypal.me/PiMachowski" target="_blank"><img src="https://www.paypalobjects.com/webstatic/mktg/logo/pp_cc_mark_37x23.jpg" border="0" alt="PayPal Logo" style="height: auto !important;width: auto !important;"></a>