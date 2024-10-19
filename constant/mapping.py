MODULE_MAPPING  = {
    "dmAgent": "mad:dmAgt",
    "dmAgentAnnc": "mad:dmAgtAnnc",
    "dmDeviceInfo": "mad:dmDIo",
    "dmDeviceInfoAnnc": "mad:dmDIoAnnc",
    "dmDataModelIO": "mad:dDMIO",
    "dmDataModelIOAnnc": "mad:dDMIOAnnc",
    "dmFirmware": "mad:dmFie",
    "dmFirmwareAnnc": "mad:dmFieAnnc",
    "dmSoftware": "mad:dmSoe",
    "dmSoftwareAnnc": "mad:dmSoeAnnc",
    "dmEventLog": "mad:dmELg",
    "dmEventLogAnnc": "mad:dmELgAnnc",
    "dmPackage": "mad:dmPae",
    "dmPackageAnnc": "mad:dmPaeAnnc",
    "battery": "cod:bat",
    "batteryAnnc": "cod:batAnnc",
    "dmCapability": "mad:dmCay",
    "dmCapabilityAnnc": "mad:dmCayAnnc",
    "dmStorage": "mad:dmSte",
    "dmStorageAnnc": "mad:dmSteAnnc",
    "dmAreaNwkInfo": "mad:dANIo",
    "dmAreaNwkInfoAnnc": "mad:dANIoAnnc",
}

def get_module_mapping(module_name):
    return MODULE_MAPPING.get(module_name, module_name)