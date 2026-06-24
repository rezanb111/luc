import os
import time
import asyncio
import httpx

PHPSESSID = os.getenv("PHPSESSID", "30cq8m0qaesn0qa71n3v0scam8")
PARTNER_ID = os.getenv("PARTNER_ID", "544787")
HASH_VAL = os.getenv("HASH_VAL", "87b414b8e9b44018e69c49705bdda8b4")
ANTICAPTCHA_KEY = "3e6ee8f7b20673e0bea1954c1a1dca1b"

BASE_URL = "https://luckywatch.pro"

COOKIES = {
    'i18n_language': 'en',
    'partner': PARTNER_ID,
    'source': 'partner',
    'hash': HASH_VAL,
    'signed': '1',
    'newUser': '1'
}

if PHPSESSID:
    COOKIES['PHPSESSID'] = PHPSESSID

HEADERS_BASE = {
    "sec-ch-ua": '"Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
}

HEADERS_MAIN = {
    **HEADERS_BASE,
    "authority": "luckywatch.pro",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "fa-IR,fa;q=0.9",
    "cache-control": "max-age=0",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
}

HEADERS_API = {
    **HEADERS_BASE,
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fa-IR,fa;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': BASE_URL,
    'referer': f'{BASE_URL}/watch',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
}

HEADERS_ASSET = {
    **HEADERS_BASE,
    "Referer": f"{BASE_URL}/home",
    "Origin": BASE_URL,
}

HEADERS_IMAGE = {
    **HEADERS_BASE,
    "Referer": f"{BASE_URL}/home",
}

URL_START = f'{BASE_URL}/api/user/tasks/start/'
URL_CLAIM = f'{BASE_URL}/api/user/captcha/check/'
URL_GET_TASK = f'{BASE_URL}/api/user/tasks/'

PATHS = [
    ("_nuxt/entry.C5FSZmZw.css", HEADERS_ASSET),
    ("_nuxt/ContestBanner.CjldQDDa.css", HEADERS_ASSET),
    ("_nuxt/Card.PAQBrh0V.css", HEADERS_ASSET),
    ("_nuxt/AboutCloverCoinsModal.BNk0e1Iy.css", HEADERS_ASSET),
    ("_nuxt/Ticket.BEOCOE3Z.css", HEADERS_ASSET),
    ("_nuxt/home.v1AWlsSb.css", HEADERS_ASSET),
    ("_nuxt/DailyActivityBonus.DMFVvgQe.css", HEADERS_ASSET),
    ("_nuxt/TabsButtons.C1SgoviN.css", HEADERS_ASSET),
    ("_nuxt/CMKNj3A3.js", HEADERS_ASSET),
    ("_nuxt/DtsBHWkf.js", HEADERS_ASSET),
    ("_nuxt/DI8PmBzh.js", HEADERS_ASSET),
    ("_nuxt/D8lLvQJG.js", HEADERS_ASSET),
    ("_nuxt/ChmaW0go.js", HEADERS_ASSET),
    ("_nuxt/DcmLabxQ.js", HEADERS_ASSET),
    ("_nuxt/C2H3mdrr.js", HEADERS_ASSET),
    ("_nuxt/CqCgU2Uw.js", HEADERS_ASSET),
    ("_nuxt/CzswSHGS.js", HEADERS_ASSET),
    ("_nuxt/B3dDciVO.js", HEADERS_ASSET),
    ("_nuxt/C7khifH4.js", HEADERS_ASSET),
    ("_nuxt/DNm_PIF_.js", HEADERS_ASSET),
    ("_nuxt/gVsmFxI3.js", HEADERS_ASSET),
    ("_nuxt/CsAs0ql9.js", HEADERS_ASSET),
    ("_nuxt/DDewvqQR.js", HEADERS_ASSET),
    ("_nuxt/CWA2liGQ.js", HEADERS_ASSET),
    ("_nuxt/C1Wiwm26.js", HEADERS_ASSET),
    ("_nuxt/C4DQ14k_.js", HEADERS_ASSET),
    ("_nuxt/DZ_KPAKH.js", HEADERS_ASSET),
    ("_nuxt/CRrb34_1.js", HEADERS_ASSET),
    ("_nuxt/BboZT6Jk.js", HEADERS_ASSET),
    ("_nuxt/CEuQGtZT.js", HEADERS_ASSET),
    ("_nuxt/BzPTsZqq.js", HEADERS_ASSET),
    ("_nuxt/D7s0jCAl.js", HEADERS_ASSET),
    ("_nuxt/CXy68sSw.js", HEADERS_ASSET),
    ("_nuxt/BwPD5xlT.js", HEADERS_ASSET),
    ("_nuxt/BgMdMfFk.js", HEADERS_ASSET),
    ("_nuxt/BFhgy7TN.js", HEADERS_ASSET),
    ("_nuxt/fsX-agm_.js", HEADERS_ASSET),
    ("_nuxt/B09UubrD.js", HEADERS_ASSET),
    ("_nuxt/C3NQFOAa.js", HEADERS_ASSET),
    ("_nuxt/BqCA_dUZ.js", HEADERS_ASSET),
    ("_nuxt/BBAMlSAs.js", HEADERS_ASSET),
    ("_nuxt/BTEVilN4.js", HEADERS_ASSET),
    ("_nuxt/DfVvgsPE.js", HEADERS_ASSET),
    ("_nuxt/DD-lmcTp.js", HEADERS_ASSET),
    ("_nuxt/Bhp_3j9C.js", HEADERS_ASSET),
    ("_nuxt/DWUkkhob.js", HEADERS_ASSET),
    ("_nuxt/BoakHOiZ.js", HEADERS_ASSET),
    ("_nuxt/D_J0b50S.js", HEADERS_ASSET),
    ("_nuxt/cU90o9JF.js", HEADERS_ASSET),
    ("_nuxt/DpGP5nS5.js", HEADERS_ASSET),
    ("_nuxt/DPH66DLL.js", HEADERS_ASSET),
    ("_nuxt/B_c9_-1V.js", HEADERS_ASSET),
    ("_nuxt/usGaLRjO.js", HEADERS_ASSET),
    ("_nuxt/DwcLuAsc.js", HEADERS_ASSET),
    ("_nuxt/BXKQtvhJ.js", HEADERS_ASSET),
    ("_nuxt/BVgY3g44.js", HEADERS_ASSET),
    ("_nuxt/DyTBKMIB.js", HEADERS_ASSET),
    ("_nuxt/Cg85v4f3.js", HEADERS_ASSET),
    ("_nuxt/Dyc4RYKS.js", HEADERS_ASSET),
    ("_nuxt/Boaz5yts.js", HEADERS_ASSET),
    ("_nuxt/B7KjyWPW.js", HEADERS_ASSET),
    ("_nuxt/DmjDB72w.js", HEADERS_ASSET),
    ("builds/meta/2859b214-32e2-4eb4-ab0b-5f848817df82.json", HEADERS_ASSET),
    ("images/user.svg", HEADERS_IMAGE),
    ("images/contest/clover_green.webp", HEADERS_IMAGE),
    ("_nuxt/EnBnPtYp.js", HEADERS_ASSET),
    ("_nuxt/baCgqCqF.js", HEADERS_ASSET),
    ("_nuxt/Dx9HRPxD.js", HEADERS_ASSET),
    ("_nuxt/BqW7qvuL.js", HEADERS_ASSET),
    ("_nuxt/Dj022kuZ.js", HEADERS_ASSET),
    ("_nuxt/BkFigO_R.js", HEADERS_ASSET),
    ("_nuxt/D7_1iARt.js", HEADERS_ASSET),
    ("_nuxt/B5J6AIJi.js", HEADERS_ASSET),
    ("_nuxt/BwtSNsM6.js", HEADERS_ASSET),
    ("_nuxt/Wp1A14sF.js", HEADERS_ASSET),
]

async def solve_captcha_base64(client, base64_string):
    try:
        payload = {
            "clientKey": ANTICAPTCHA_KEY,
            "task": {
                "type": "ImageToTextTask",
                "body": base64_string,
                "phrase": False,
                "case": False,
                "numeric": 0,
                "math": False,
                "minLength": 0,
                "maxLength": 0
            }
        }
        res = await client.post("https://api.anti-captcha.com/createTask", json=payload, timeout=20.0)
        if res.status_code == 200 and "taskId" in res.json():
            task_id = res.json()["taskId"]
            for _ in range(20):
                await asyncio.sleep(3)
                result_res = await client.post("https://api.anti-captcha.com/getTaskResult", json={"clientKey": ANTICAPTCHA_KEY, "taskId": task_id}, timeout=20.0)
                if result_res.status_code == 200:
                    data = result_res.json()
                    if data.get("status") == "ready":
                        return data["solution"]["text"]
    except Exception:
        pass
    return None

async def get_active_task(client):
    try:
        res = await client.post(URL_GET_TASK, data='method=get&mac=0', timeout=10.0)
        if res.status_code == 200:
            data = res.json()
            if isinstance(data, dict) and 'id' in data:
                return data.get('id')
            elif isinstance(data, list) and len(data) > 0:
                return data[0].get('id')
    except Exception:
        pass
    return "366955"

async def fetch_asset(client, path, headers):
    url = f"{BASE_URL}/{path.lstrip('/')}"
    try:
        await client.get(url, headers=headers)
    except Exception:
        pass

async def load_site_assets(client):
    tasks = [fetch_asset(client, path, hdrs) for path, hdrs in PATHS]
    await asyncio.gather(*tasks)

async def run_loop(client):
    await client.get(f"{BASE_URL}/home", headers=HEADERS_MAIN)
    await load_site_assets(client)
    
    task_id = await get_active_task(client)
    print(f"[*] Task: {task_id}")
    
    payload_start = f"TaskId={task_id}&fin%5BvideoCard%5D%5Bvendor%5D=Google+Inc.+%28ARM%29&fin%5BvideoCard%5D%5Brenderer%5D=ANGLE+%28ARM%2C+Mali-G57+MC2%2C+OpenGL+ES+3.2%29&fin%5BviewPort%5D%5Bh%5D=648&fin%5BviewPort%5D%5Bw%5D=349&fin%5BviewPort%5D%5BhM%5D=854&fin%5BviewPort%5D%5BwM%5D=384&fin%5Bplatform%5D=Linux+armv81&fin%5Bdpr%5D=3.0921943187713623&fin%5Bmulti%5D%5Bspeakers%5D=1&fin%5Bmulti%5D%5Bmicros%5D=1&fin%5Bmulti%5D%5Bwebcams%5D=2&fin%5Bmulti%5D%5Bdevices%5D=1&fin%5Bori%5D%5Balpha%5D=179.20000000000002&fin%5Bori%5D%5Bbeta%5D=141.9&fin%5Bori%5D%5Bgamma%5D=-53.2&fin%5Bori%5D%5Bis%5D=1&fin%5Bv%5D=2.6&fin%5Bcl%5D%5Bx%5D=61&fin%5Bcl%5D%5By%5D=33&fin%5BwebDef%5D=false&fin%5BnavName%5D=Navigator&fin%5Btouch%5D=true&fin%5Bc%5D=137&fin%5Bmemory%5D=8&fin%5Bconcur%5D=8&fin%5Ben%5D%5Bar%5D=&fin%5Ben%5D%5Bb%5D=137&fin%5Ben%5D%5Bm%5D=24117RN76G&fin%5Ben%5D%5Bp%5D=Android&fin%5Ben%5D%5Bpv%5D=15.0.0&fin%5Bbat%5D%5Bcharging%5D=1&fin%5Bbat%5D%5Blvl%5D=0.51"
    
    try:
        res_start = await client.post(URL_START, data=payload_start, headers=HEADERS_API, timeout=15.0)
        if res_start.status_code == 200:
            print("[✓] Task started. Wait 36s...")
            await asyncio.sleep(36)
            
            res_claim = await client.post(URL_CLAIM, data='refreshTask=0', headers=HEADERS_API, timeout=15.0)
            if res_claim.status_code == 200:
                resp_json = res_claim.json()
                
                if resp_json.get("status") == "data" and "data" in resp_json and "image" in resp_json["data"]:
                    print("[!] Captcha detected. Solving...")
                    raw_base64 = resp_json["data"]["image"]
                    captcha_text = await solve_captcha_base64(client, raw_base64)
                    
                    if captcha_text:
                        print(f"[✓] Solved: {captcha_text}")
                        payload_captcha = f"refreshTask=0&captcha={captcha_text}"
                        res_final = await client.post(URL_CLAIM, data=payload_captcha, headers=HEADERS_API, timeout=15.0)
                        print(f"[✓] Response: {res_final.text}")
                    else:
                        print("[!] Solver failed.")
                else:
                    print(f"[✓] Claimed: {res_claim.text}")
            else:
                print(f"[!] Claim error: {res_claim.status_code}")
        else:
            print(f"[!] Start error: {res_start.status_code}")
    except Exception as error:
        print(f"[!] Network error: {error}")

async def main():
    limits = httpx.Limits(max_keepalive_connections=10, max_connections=20)
    async with httpx.AsyncClient(limits=limits, cookies=COOKIES, timeout=15.0) as client:
        while True:
            await run_loop(client)
            await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())
