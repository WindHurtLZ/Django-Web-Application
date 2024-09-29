import logging
import uuid
import requests

from core import settings

logger = logging.getLogger(__name__)

def generate_request_identifier():
    return str(uuid.uuid4())

def register_web():

    cse_url = settings.ONE_M2M_CSE_URL
    request_identifier = generate_request_identifier()

    headers = {
        "X-M2M-Origin": settings.ONE_M2M_ORIGINATOR,
        "X-M2M-RI": request_identifier,
        "X-M2M-RVI": "3",
        "Content-Type": "application/json;ty=2",
        "Accept": "application/json",
    }

    data = {
        "m2m:ae": {
            "rn": settings.ONE_M2M_AE_NAME,
            "api": settings.ONE_M2M_AE_API,
            "rr": True,
            "srv": settings.ONE_M2M_AE_SRVS,
        }
    }

    try:
        response = requests.post(cse_url, headers=headers, json=data, timeout=10)
        if response.status_code in [200, 201]:
            logger.info("WebApp successfully registered")
            return True
        else:
            logger.error(f"WebApp failed to register: {response.status_code}, {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        logger.error(f"Exception occur during WebApp AE registration{e}")
        return False

def check_register_web():
    request_identifier = generate_request_identifier()
    web_url = f"{settings.ONE_M2M_CSE_URL}/{settings.ONE_M2M_AE_NAME}"

    headers = {
        "X-M2M-Origin": settings.ONE_M2M_ORIGINATOR,
        "X-M2M-RI": request_identifier,
        "X-M2M-RVI": "3",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    try:
        response = requests.get(web_url, headers=headers, timeout=10)
        if response.status_code == 200:
            logger.info("WebApp AE is already registered")
            return True
        else:
            logger.warning(f"WebApp AE is not registered: {response.status_code}, {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        logger.error(f"Exception occur during retrieving WebApp AE registration info: {e}")
        return False

def job_register_web():
    if not check_register_web():
        register_success = register_web()
        if not register_success:
            logger.error("job_register_web: WebApp AE registration failed")
        else:
            logger.info("job_register_web: WebApp AE registration successful")
    else:
        logger.info("job_register_web: WebApp AE registration already registered")

def register_device_ae(device):

    cse_url = settings.ONE_M2M_CSE_URL
    request_identifier = generate_request_identifier()

    device_name_no_spaces = "".join(device.name.split())
    originator = f"C{device.type}_{str(device.ae_id)[:8]}"
    ae_rn = device.ae_rn
    ae_api = f"N{device.ae_rn}"

    headers = {
        "X-M2M-Origin": originator,
        "X-M2M-RI": request_identifier,
        "X-M2M-RVI": "3",
        "Content-Type": "application/json;ty=2",
        "Accept": "application/json",
    }

    data = {
        "m2m:ae": {
            "rn": ae_rn,
            "api": ae_api,
            "rr": True,
            "srv": settings.ONE_M2M_AE_SRVS,
        }
    }

    try:
        response = requests.post(cse_url, headers=headers, json=data, timeout=10)
        logger.debug(f"Received response: {response.status_code}, {response.text}")
        if response.status_code in [200, 201, 403, 409]:
            if response.status_code in [403, 409]:
                logger.warning(f"Device AE already exists: {response.status_code}, {response.text}")
            else:
                logger.info("Device AE successfully registered")

                container_rn = "data"
                container_creation_success = create_data_container(cse_url, ae_rn, container_rn, originator)
                if container_creation_success:
                    logger.info(f"Data container '{container_rn}' created for AE '{ae_rn}'")

                    subscription_success = create_subscription(cse_url, ae_rn, originator, settings.ONE_M2M_NOTIFICATIONS_URL)
                    if subscription_success:
                        logger.info(f"Subscription created for container '{container_rn}' of AE '{ae_rn}'")
                    else:
                        logger.error(f"Failed to create subscription for container '{container_rn}' of AE '{ae_rn}'")
                else:
                    logger.error(f"Failed to create data container '{container_rn}' for AE '{ae_rn}'")



            return True, ae_rn, originator
        else:
            logger.error(f"Device AE failed to register: {response.status_code}, {response.text}")
            return False, None, None

    except requests.exceptions.RequestException as e:
        logger.error(f"Exception occur during Device AE registration: {e}")
        return False, None, None

def create_data_container(cse_url, ae_rn, container_rn, originator):

    container_url = f"{cse_url}/{ae_rn}"
    request_identifier = generate_request_identifier()

    headers = {
        "X-M2M-Origin": originator,
        "X-M2M-RI": request_identifier,
        "X-M2M-RVI": "3",
        "Content-Type": "application/json;ty=3",
        "Accept": "application/json",
    }

    data = {
        "m2m:cnt": {
            "rn": container_rn,
        }
    }

    try:
        response = requests.post(container_url, headers=headers, json=data, timeout=10)
        logger.debug(f"Received response for container creation: {response.status_code}, {response.text}")
        if response.status_code in [200, 201, 403, 409]:
            if response.status_code in [403, 409]:
                logger.warning(f"Container '{container_rn}' already exists: {response.status_code}, {response.text}")
            else:
                logger.info(f"Container '{container_rn}' successfully created")
            return True
        else:
            logger.error(f"Container '{container_rn}' failed to create: {response.status_code}, {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        logger.error(f"Exception occur during Container creation: {e}")
        return False

def create_subscription(cse_url, ae_rn, originator, notification_url):

    subscription_rn = f"{ae_rn}Subscription"
    request_identifier = generate_request_identifier()

    headers = {
        "X-M2M-Origin": originator,
        "X-M2M-RI": request_identifier,
        "X-M2M-RVI": "3",
        "Content-Type": "application/json;ty=23",  # ty=23 表示订阅资源
        "Accept": "application/json",
    }

    data = {
        "m2m:sub": {
            "rn": subscription_rn,
            "nu": [notification_url],
            "nct": 1,
            "enc": {
                "net": [3],
            },
        }
    }

    try:
        subscription_url = f"{cse_url}/{ae_rn}/data"
        response = requests.post(subscription_url, headers=headers, json=data)
        logger.debug(f"Subscription response: {response.status_code}, {response.text}")
        if response.status_code in [200, 201, 202]:
            logger.info(f"Subscription '{subscription_rn}' created successfully for AE '{ae_rn}'")
            return True
        else:
            logger.error(f"Failed to create subscription '{subscription_rn}': {response.status_code}, {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        logger.error(f"Exception occur during subscription creation: {e}")
        return False