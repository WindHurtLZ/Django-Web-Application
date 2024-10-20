MODULE_MAPPING = {
    "dmAgent": {
        "short_name": "mad:dmAgt",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmAgentAnnc": {
        "short_name": "mad:dmAgtAnnc",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmDeviceInfo": {
        "short_name": "mad:dmDIo",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmDeviceInfoAnnc": {
        "short_name": "mad:dmDIoAnnc",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmDataModelIO": {
        "short_name": "mad:dDMIO",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmDataModelIOAnnc": {
        "short_name": "mad:dDMIOAnnc",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmFirmware": {
        "short_name": "mad:dmFie",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmFirmwareAnnc": {
        "short_name": "mad:dmFieAnnc",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmSoftware": {
        "short_name": "mad:dmSoe",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmSoftwareAnnc": {
        "short_name": "mad:dmSoeAnnc",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmEventLog": {
        "short_name": "mad:dmELg",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmEventLogAnnc": {
        "short_name": "mad:dmELgAnnc",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmPackage": {
        "short_name": "mad:dmPae",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmPackageAnnc": {
        "short_name": "mad:dmPaeAnnc",
        "attributes": {},
        "cnd_type": "management"
    },
    "battery": {
        "short_name": "cod:bat",
        "attributes": {},
        "cnd_type": "management"
    },
    "batteryAnnc": {
        "short_name": "cod:batAnnc",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmCapability": {
        "short_name": "mad:dmCay",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmCapabilityAnnc": {
        "short_name": "mad:dmCayAnnc",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmStorage": {
        "short_name": "mad:dmSte",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmStorageAnnc": {
        "short_name": "mad:dmSteAnnc",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmAreaNwkInfo": {
        "short_name": "mad:dANIo",
        "attributes": {},
        "cnd_type": "management"
    },
    "dmAreaNwkInfoAnnc": {
        "short_name": "mad:dANIoAnnc",
        "attributes": {},
        "cnd_type": "management"
    },
    "lock": {
        "short_name": "cod:lock",
        "attributes": {
            "lock": True
        },
        "cnd_type": "common"
    },
}

def get_module_mapping(module_name):
    return MODULE_MAPPING.get(module_name, {"short_name": module_name, "attributes": {}, "cnd_type": "management"})
