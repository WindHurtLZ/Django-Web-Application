from datetime import datetime

MODULE_MAPPING = {
    "dmAgent": {
        "short_name": "mad:dmAgt",
        "attributes": {
            "state": 4
        },
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "dmAgentAnnc": {
        "short_name": "mad:dmAgtAnnc",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclassAnnc"
    },
    # Action: reboot
    "reboot": {
        "short_name": "mad:rebot",
        "attributes": {
            "dgt": None,
            "rebTe": 1
        },
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "action"
    },


    "dmDeviceInfo": {
        "short_name": "mad:dmDIo",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "dmDeviceInfoAnnc": {
        "short_name": "mad:dmDIoAnnc",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclassAnnc"
    },
    "dmDataModelIO": {
        "short_name": "mad:dDMIO",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "dmDataModelIOAnnc": {
        "short_name": "mad:dDMIOAnnc",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclassAnnc"
    },
    "dmFirmware": {
        "short_name": "mad:dmFie",
        "attributes": {
            "mulFe": False,
            "priSe": 1,
            "priNe": "primary firmware name",
            "priVn": "primary firmware version"
        },
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "dmFirmwareAnnc": {
        "short_name": "mad:dmFieAnnc",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclassAnnc"
    },
    # Action: updateFirmware
    "updateFirmware": {
        "short_name": "mad:updFe",
        "attributes": {
            "dgt": None,
            "resut": "New Resource"
        },
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "action"
    },

    "dmSoftware": {
        "short_name": "mad:dmSoe",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "dmSoftwareAnnc": {
        "short_name": "mad:dmSoeAnnc",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclassAnnc"
    },
    "dmEventLog": {
        "short_name": "mad:dmELg",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "dmEventLogAnnc": {
        "short_name": "mad:dmELgAnnc",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclassAnnc"
    },
    "dmPackage": {
        "short_name": "mad:dmPae",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "dmPackageAnnc": {
        "short_name": "mad:dmPaeAnnc",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclassAnnc"
    },
    "battery": {
        "short_name": "cod:bat",
        "attributes": {
            "lvl": 0,
            "lowBy": True
        },
        "cnd_type": "common",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "batteryAnnc": {
        "short_name": "cod:batAnnc",
        "attributes": {},
        "cnd_type": "common",
        "domain": "onem2m",
        "type": "moduleclassAnnc"
    },
    "dmCapability": {
        "short_name": "mad:dmCay",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "dmCapabilityAnnc": {
        "short_name": "mad:dmCayAnnc",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclassAnnc"
    },
    "dmStorage": {
        "short_name": "mad:dmSte",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "dmStorageAnnc": {
        "short_name": "mad:dmSteAnnc",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclassAnnc"
    },
    "dmAreaNwkInfo": {
        "short_name": "mad:dANIo",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "dmAreaNwkInfoAnnc": {
        "short_name": "mad:dANIoAnnc",
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclassAnnc"
    },
    "lock": {
        "short_name": "cod:lock",
        "attributes": {
            "lock": True
        },
        "cnd_type": "common",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "bikeData": {
        "short_name": "bdm:bikDt",
        "attributes": {
            "latie": 0.0,
            "longe": 0.0,
            "speed": 0.0,
            "tempe": 0.0,
            "accel": 0.0
        },
        "cnd_type": "bike",
        "domain": "onem2m",
        "type": "moduleclass"
    },
    "meshConnectivity": {
        "short_name": "bdm:msCoy",
        "attributes": {
            "neibo": "Neighbor ID",
            "rssi": 0
        },
        "cnd_type": "bike",
        "domain": "onem2m",
        "type": "moduleclass"
    },
}

def get_current_timestamp():
    # ISO 8601 data time
    return datetime.now().isoformat(timespec='milliseconds') + "Z"

def get_module_mapping(module_name):
    default_mapping = {
        "short_name": module_name,
        "attributes": {},
        "cnd_type": "management",
        "domain": "onem2m",
        "type": "moduleclass"
    }

    module_mapping = MODULE_MAPPING.get(module_name, {})

    # Set Data Time
    if "dgt" in module_mapping.get("attributes", {}):
        module_mapping["attributes"]["dgt"] = get_current_timestamp()

    return {**default_mapping, **module_mapping}