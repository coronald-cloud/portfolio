"""
Portfolio Image Downloader
Downloads all 73 images from ronaldconnthe3rd.myportfolio.com
Saves them directly into this folder (alongside index.html)

Run with:  python download_images.py
"""

import urllib.request
import os
import time

BASE = "https://cdn.myportfolio.com/57e76d22-b0a1-4eee-a589-39268204d340/"

IMAGES = [
    ("0ebdcb71-12de-4936-857f-52bef9a2b9e1_car_202x158.png?h=0e028a4f49e2a0f1a312bb0e51bbac25", "uiux-website-design-standby-detroit_01.png"),
    ("d354c7a4-06e5-4c76-b94d-fcd742a67ca4_rw_1920.png?h=605c561c2e240df8a7134173368622bf", "uiux-website-design-standby-detroit_02.png"),
    ("0ae19186-5683-4f84-9801-742d95f59e1d_rw_1920.png?h=82d4ec3d747c56fa96c9e93938515ef4", "uiux-website-design-standby-detroit_03.png"),
    ("20d68a93-62c9-4c1b-a474-5a84d7f97e95_rw_1920.png?h=c824854b83f0020d2330d1c0e8b1636c", "uiux-website-design-standby-detroit_04.png"),
    ("df4432db-e904-4192-be72-25185a79e436_car_202x158.png?h=4aedaab2aeb05b5fd796f50df5000d28", "uiux-redbull-soundclash_01.png"),
    ("97018d3d-0113-4187-915e-a53a9bdd8e5e_rw_1920.png?h=93914ab10ad3eb8ce9a42b50425c93fb", "uiux-redbull-soundclash_02.png"),
    ("5fa78056-cfa7-4459-bb7d-376ed58e9ab3_rw_1920.png?h=121dce6cccb73ff20dcde7cfd7e09b79", "uiux-redbull-soundclash_03.png"),
    ("b7431a6e-e060-48d7-bf17-d55c4a095d53_rw_1920.png?h=1d5eb7d6221cb53af3ada761a423b801", "uiux-redbull-soundclash_04.png"),
    ("9064d880-f67b-40e5-a31f-605b19ebefe1_rw_1920.png?h=0d9c4bf84c17f1346539596e058c5e7d", "uiux-redbull-soundclash_05.png"),
    ("815a927b-d71c-4164-9bb7-a99ecb05c0e6_rw_1920.png?h=55308ba59ee7b69ba38dfc54bb50671b", "uiux-redbull-soundclash_06.png"),
    ("fc48b869-3f48-4519-93ef-a64f64f13372_rw_1920.png?h=be1208f425e3518fcb99a2a972ac2bbf", "uiux-redbull-soundclash_07.png"),
    ("7e8416eb-ca8d-4ae2-9835-100f36e1cc9b_car_202x158.jpg?h=275f0d2707be31274e3d69ba06d8c231", "wellflower-custom-illustrated-murals_01.jpg"),
    ("4054a0b5-3fc9-4400-a178-67e2d871026f_rw_1920.jpg?h=b217ec2873eaebc79181d1e5ffbe1a0a", "wellflower-custom-illustrated-murals_02.jpg"),
    ("0028a0ae-85ed-4120-95d0-0c46bd1e0b9d_rw_1920.jpg?h=88d4cba9358d6ee892e120befe60b75c", "wellflower-custom-illustrated-murals_03.jpg"),
    ("6d89d71c-06d7-4cb8-bd70-c932eb928110_rw_1920.jpg?h=effd59dae42235b4857c4993aa89ebe0", "wellflower-custom-illustrated-murals_04.jpg"),
    ("1f33bb4f-11d1-4274-86f3-5626c20dba51_rw_1920.jpg?h=9cc22ae57abc790de88a4ff74a89ec2f", "wellflower-custom-illustrated-murals_05.jpg"),
    ("e65d8688-4ff3-451c-8518-f0de5877f72d_rw_1920.jpg?h=0320ed8fc5846d4c5072df6b0c231886", "wellflower-custom-illustrated-murals_06.jpg"),
    ("40904074-e6c4-40ca-ad3e-dd957e964406_car_202x158.png?h=39dc2b0e67631d5dd1b4dcf7e36cd175", "web-design-the-wellflower-group_01.png"),
    ("de71525d-3403-49fa-9b06-d9fbcd716b68_rw_1920.png?h=c8b33035561e7460736a31cb7a6d1f90", "web-design-the-wellflower-group_02.png"),
    ("767dc89c-9892-40b3-b19c-5d23aac21af2_rw_1920.png?h=6f733207e58a2980f0fca08b50da7db4", "web-design-the-wellflower-group_03.png"),
    ("6c98d0d4-b981-4b42-b14d-ab8305ac342d_rw_1920.png?h=c9b33d8ea17fb73f741fda60cafd1856", "web-design-the-wellflower-group_04.png"),
    ("0bc373e7-804f-4421-9be5-020ee697b1d1_car_202x158.png?h=1acc8002d2a2346c8450d4d3d4a16acd", "packaging-design-wellflower-group_01.png"),
    ("fa654d63-ac4e-47d7-a591-0b49c2ac1146_rw_1920.png?h=2f313e92511e9a425f64418b6519a74b", "packaging-design-wellflower-group_02.png"),
    ("d7359fd4-2874-43ce-a237-07df3d0b79c8_rw_1920.png?h=387df654a6fd7819dcddf0f099a9f9c7", "packaging-design-wellflower-group_03.png"),
    ("566ae090-8e17-4dcf-b488-575741d1acd5_rw_1920.jpg?h=564902990fafa42859e4beabcd7ee993", "packaging-design-wellflower-group_04.jpg"),
    ("178cfc35-9c05-4d92-8fd2-7f74d4816a08_car_202x158.png?h=b412a9edbf08a149019e0c3ed04cdbe3", "redbull-dance-your-style-graphics_01.png"),
    ("6dc6a652-8cc8-4dcb-a29f-914ec4d5d00e_rw_1920.png?h=86bce367088a3a40ea8a1e36ed03608b", "redbull-dance-your-style-graphics_02.png"),
    ("db823798-c01b-4a74-bbd9-4250a7daafc4_rw_1920.png?h=267ff15b57a4a74e3d10ae8901fd8e84", "redbull-dance-your-style-graphics_03.png"),
    ("7a615b6a-f3a3-4b04-8136-396243b20f97_rw_1920.png?h=4244f905e42c236338a5ad99352dbc3f", "redbull-dance-your-style-graphics_04.png"),
    ("a99d99df-f062-44bc-abb3-e5696beeca33_rw_1920.png?h=fac8b0b811ceb6a18bd89c50a7071e9f", "redbull-dance-your-style-graphics_05.png"),
    ("dfa9dc79-94c4-4d4f-92b0-3618fac13591_car_202x158.png?h=6f00edf45d6038e0ce667df9829b71db", "redbull-heavy-metal-artwork-and-map_01.png"),
    ("6c7c97b2-d015-4836-ac1d-80f2c2b69930_rw_1200.png?h=6771960b72857477b0a093c9349d5106", "redbull-heavy-metal-artwork-and-map_02.png"),
    ("14ee81b0-6f72-4b27-b342-d14cd086d009_rw_1200.jpg?h=1b2742914a915f46c5643cf4eb38d328", "redbull-heavy-metal-artwork-and-map_03.jpg"),
    ("1e23dbea-efcf-496f-a9dd-36073881b37c_rw_1200.jpg?h=73c21a5811ff1f1507cd4740b74a0340", "redbull-heavy-metal-artwork-and-map_04.jpg"),
    ("68081c4c-9663-46b4-8fb3-4c6a96c0f0ac_rw_1200.jpg?h=9eed3b55e4cc3a246f36c9d66b1b320e", "redbull-heavy-metal-artwork-and-map_05.jpg"),
    ("c3af2b3b-c899-437a-8273-7b6925a7a907_rw_1920.jpg?h=7f095b406100c0d26dc8dd21eba95b7b", "redbull-heavy-metal-artwork-and-map_06.jpg"),
    ("833762ae-e67a-4efe-8ff0-61feb5526e25_rw_1920.jpg?h=2498e3926151173d559c56f313dc7418", "redbull-heavy-metal-artwork-and-map_07.jpg"),
    ("6bc16869-63aa-4a2a-b852-b70afc120c8c_car_202x158.jpg?h=f1504dcbca0efd01cbc65252db328c2f", "redbull-soundclash_01.jpg"),
    ("105e53e1-3cf0-436e-88c7-e0113cd84496_rw_1920.jpg?h=3dba0888c63c7ab5f850222a7e21870b", "redbull-soundclash_02.jpg"),
    ("8593d8bd-5f37-41ed-908c-e593ae7420ae_rw_1920.jpg?h=e13902539719f045e3f5261fa9eb2f7b", "redbull-soundclash_03.jpg"),
    ("4084aebd-5a50-4741-9281-f659e7cb6bbe_rw_1920.jpg?h=06a5b51e41faac69e64f7cce1f0b545a", "redbull-soundclash_04.jpg"),
    ("656258af-b52b-40eb-821e-e7e2f7676b34_rw_1200.jpg?h=ef81de0db1d974d9a890091d4c1d68a2", "redbull-soundclash_05.jpg"),
    ("6fbdc7ad-a3b3-4d1a-a779-7aec3774f5a4_rw_1920.png?h=82df2a022e9ce82b756d4534c1d5d58d", "redbull-soundclash_06.png"),
    ("27a9e0d5-98e2-4b19-8c1f-5150a4f49bd8_rw_1920.jpg?h=23b01454404add74b613ddfcf83ad8de", "redbull-soundclash_07.jpg"),
    ("8190af7b-5571-44ab-8405-d6d209588f0f_rw_1920.jpg?h=2ded2dd51d3a649f77b524a8fdaf7f98", "redbull-soundclash_08.jpg"),
    ("257f8379-ed57-4241-ac50-df135224f475_rw_1200.jpg?h=ef4bea94fb784e59d91110d9625a9b78", "redbull-soundclash_09.jpg"),
    ("566602fb-3b53-4dec-bdd7-ef9f44441292_rw_1200.jpg?h=f53b7420f3e9b162c70f8bce1b63675e", "redbull-soundclash_10.jpg"),
    ("f9bdb912-dbea-4bee-8c0a-d731c7dcd6e5_rw_1200.jpg?h=1761ebead7e8fe59b7a27a0597d06129", "redbull-soundclash_11.jpg"),
    ("9bf7c428-9372-490c-aa82-e14e9a20dba2_rw_1920.png?h=25959a518282448540c8628c091094d9", "redbull-soundclash_12.png"),
    ("b4da96bd-8264-465c-832f-66404eaf9d7b_rw_1920.png?h=f0d3b7468a143a3552cb6af2685931e2", "redbull-soundclash_13.png"),
    ("faa9d0bc-513a-4374-bf4e-3b628b394c67_car_202x158.jpg?h=fd07f51baef16ba3ab819e7ff3350c66", "wellflower-retail-interior-design_01.jpg"),
    ("695ec7c6-684f-4ac1-ae73-d96efed58317_rw_1920.jpg?h=4a59d60b9f02c6ec5bb08b494ed56ce8", "wellflower-retail-interior-design_02.jpg"),
    ("c69d23cf-1183-430e-888f-4a53a9043fa5_rw_1920.jpg?h=8961dcc06f3de1762653a6fe01059bc8", "wellflower-retail-interior-design_03.jpg"),
    ("bfbd11ac-42f5-4fdb-b81f-ae6604d2b8cd_rw_1920.jpg?h=d889333915c12ee858a5fa53a86c79d6", "wellflower-retail-interior-design_04.jpg"),
    ("df43541d-d262-413a-81f8-7496a1016368_rw_1920.jpg?h=6e1d0ac6db26c1b2ded6a4916d4f7f71", "wellflower-retail-interior-design_05.jpg"),
    ("d0fe780c-1ab2-4a7e-a394-f7349951ae7f_rw_1920.jpg?h=29c4a805f721cc3c54fa23921a7d8b77", "wellflower-retail-interior-design_06.jpg"),
    ("92a0e553-567a-4a87-9774-5c07e87bd33e_rw_1920.jpg?h=791bd66a4a6270261b0d0ce0e5f2e89d", "wellflower-retail-interior-design_07.jpg"),
    ("c24b17e5-185e-4c66-addd-384cac2e277b_rw_1920.jpg?h=3a5fdeb3960e155c560c80fad7b2874c", "wellflower-retail-interior-design_08.jpg"),
    ("a58fd3ab-f400-42a3-9d44-0a318b351d87_rw_1920.jpg?h=80f357e53aa59f0c66a589ea7ace2c7d", "wellflower-retail-interior-design_09.jpg"),
    ("285017b8-af10-4b7c-8a2b-e420d351ad92_rw_1920.jpg?h=340c10cba7936e5ea77488a8cb7158ee", "wellflower-retail-interior-design_10.jpg"),
    ("80f4bf3c-8665-454a-8087-536775a6bb28_rw_1920.jpg?h=f0c9d515798f1a99652209211d269ad6", "wellflower-retail-interior-design_11.jpg"),
    ("0ba126bc-0801-4560-b854-5879cf504a33_rw_1920.jpg?h=f6f2f5d33c3741a547709dad5a1b1ac2", "wellflower-retail-interior-design_12.jpg"),
    ("2a24244b-a60d-43fa-adf4-c90dea0ad609_rw_1920.jpg?h=fcc8e2b5529b53d5d162faa1f58d91aa", "wellflower-retail-interior-design_13.jpg"),
    ("ce001d22-3ed4-4efd-9e4c-c30914e07431_rw_1920.jpg?h=fcb4df67a6125aba2b8b3cc3b529fc3a", "wellflower-retail-interior-design_14.jpg"),
    ("414c2089-0c1d-421d-85ca-359a5e1593b9_rw_1920.jpg?h=97d939df787799fffedc00db8db1b691", "wellflower-retail-interior-design_15.jpg"),
    ("38874500-e39d-4d1b-a099-2abec7d9575b_car_202x158.jpg?h=8c95157c23304fd2d0f900a207625c11", "wellflower-logo-design_01.jpg"),
    ("5669c99b-2f38-4e56-a4d3-9b1240a0c41a_rw_1920.jpg?h=6c3085a1467e9cbed6ceb7d10c83588c", "wellflower-logo-design_02.jpg"),
    ("8e198f37-c998-4b2d-a7bb-82d4f47db2d7_rw_1920.png?h=4b2937b3882548978335d99df5b67103", "wellflower-logo-design_03.png"),
    ("e37e46b6-a647-4664-a4cd-b359f3f922fd_rw_1920.jpg?h=e1958b16b097e25faf387fab43912f74", "wellflower-logo-design_04.jpg"),
    ("05cc6b56-51e0-46a0-be59-0357a54e59cc_rw_1920.jpg?h=48f3ee77791f46f7fcc2921392a4c338", "wellflower-logo-design_05.jpg"),
    ("76991527-e689-4562-a7b4-585a0a91bfb7_rw_1920.jpg?h=dea8953c6e9a9e47a208c852e34a262f", "wellflower-logo-design_06.jpg"),
    ("ce18fbac-f923-4bb8-9384-2759a5650f47_rw_1920.jpg?h=45a77d32d20f7cb6bd25cb9f6b79c9a2", "wellflower-logo-design_07.jpg"),
    ("81272e35-f13e-4432-8526-e307d0310320_rw_1920.jpg?h=6b86a22664836cc59b83d842674d265f", "wellflower-logo-design_08.jpg"),
]

# Save to same folder as this script
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

total = len(IMAGES)
success = 0
failed = []

print(f"\nDownloading {total} images to:\n{OUT_DIR}\n")

for i, (path, filename) in enumerate(IMAGES, 1):
    url = BASE + path
    dest = os.path.join(OUT_DIR, filename)

    if os.path.exists(dest):
        print(f"  [{i:02d}/{total}] Skipped (already exists): {filename}")
        success += 1
        continue

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        with open(dest, 'wb') as f:
            f.write(data)
        size_kb = len(data) // 1024
        print(f"  [{i:02d}/{total}] ✓ {filename}  ({size_kb} KB)")
        success += 1
    except Exception as e:
        print(f"  [{i:02d}/{total}] ✗ FAILED: {filename}  ({e})")
        failed.append(filename)

    time.sleep(0.1)

print(f"\n{'='*50}")
print(f"Done: {success}/{total} downloaded successfully")
if failed:
    print(f"Failed ({len(failed)}):")
    for f in failed:
        print(f"  - {f}")
print(f"Files saved to: {OUT_DIR}")
