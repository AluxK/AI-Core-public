import pyvts
# the class calling this function will need to *import asyncio


def setup_VTS(plugin_info: dict):
    vts = pyvts.vts(plugin_info=plugin_info)
    return vts


async def authenticate_connection(vts):
    await vts.connect()
    await vts.request_authenticate_token()
    await vts.request_authenticate()
    await vts.close()


async def send_VTS_request():
    vts = setup_VTS()
    await authenticate_connection(vts)
    await vts.connect()
    hotkey_list = request_hotkey_list(vts)
    hotkey_request(vts, hotkey_list)
    await vts.close()


async def request_hotkey_list(vts):
    await vts.connect()
    await authenticate_connection(vts)
    response = await vts.request(vts.vts_request.requestHotKeyList())
    hotkey_list = []
    for hotkey in response['data']['availableHotkeys']:
        hotkey_list.append(hotkey['name'])
    await vts.close()
    print(hotkey_list)
    return hotkey_list


async def hotkey_request(vts, hotkey_list):
    await vts.connect()
    await authenticate_connection(vts)
    send_hotkey_request = vts.vts_request.requestTriggerHotKey(hotkey_list)
    vts.request(send_hotkey_request)

# To run command use: asyncio.run(*function*)
