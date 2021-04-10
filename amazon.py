# # Followed this video to do this tutorial: https://www.youtube.com/watch?v=Bg9r_yLk7VY&ab_channel=DevEd

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URLs = ["https://www.amazon.com/dp/B06ZZ1MKW8/?coliid=I1S7URDP873KP1&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08G1XNG7J/ref=tmm_kin_swatch_0?_encoding=UTF8&coliid=I15CT0V01VN8S7&colid=35QH7NCHBH01U&qid=&sr=", "https://www.amazon.com/dp/B00I82884W/?coliid=I2NSN362O7FHKI&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B008CJ241O/?coliid=IAWURSJFRAQNQ&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07YKR19FN/?coliid=I1RWGHGC9RNFF8&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B005E8AS28/?coliid=I3U17KL9OKAFUD&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B0052AHUYM/?coliid=I1DRA4PKI79VBP&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B015NRKNS8/?coliid=I16X6Z2NLDJ08L&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B004ZG8VVU/?coliid=I20T2U97PYYJKH&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B071YBLDCB/?coliid=I3LFB1MYIO51DD&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B073YTDV5S/?coliid=I2LY21SGBM1JR0&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B007PHZME0/?coliid=I2HUAHSOSBXR4R&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08KZFC76K/?coliid=IZSRJ2N0S5EAM&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B0106N0W0I/?coliid=I1AT4MLG2HF9KU&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01N1MENR1/?coliid=IK73IDVLGNK5E&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01N1MENR1/?coliid=IK73IDVLGNK5E&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B079KSMJHG/?coliid=I1RC7AAM2XGRL0&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B002RLBK9A/?coliid=I2XBA49HBYKWL1&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01FZSCUKO/?coliid=I1FRWXFZCZZBK&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B009QM8M6W/?coliid=I11DWIAGE08PT4&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B000SEH42U/?coliid=I3SKJFUKBE3SRZ&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B001NLL8RO/?coliid=I1X5USYD4HVE7U&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00J1JOMYQ/?coliid=I1ID70YI57OHI3&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01HMXUSSG/?coliid=I1QANUND8PYNDH&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B000QCQ93E/?coliid=I2JSEFHCDQ9K1H&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07H453KGH/?coliid=I16G2YD3OSS9Q0&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08D1XKPQ1/?coliid=I2Y7LZLQK1R0J1&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00X2F7SWI/?coliid=I23MK1ZZTDZ753&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B005O0JNQS/?coliid=I1SRDLQE1V5OH8&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07ZTSFB5T/?coliid=I2C47SWC7IETDO&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08519CW9J/?coliid=IFS1M5IYOEGWQ&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B000FC12C8/?coliid=I33TOUZHDT1BBF&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00YBVIRDG/?coliid=I29495B9ZQ6OSF&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00AKKS278/?coliid=IYFOON5GXZOC7&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00MKZ3VUY/?coliid=I24AFXLTXHXUKO&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00R04OX20/?coliid=I1HWLBWO6RZX8O&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01EE0CQYO/?coliid=I2HYW4Z3QK829R&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B015LZ04OK/?coliid=ILEFSOZZELZXS&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01FC048RS/?coliid=IF6JUEDOVK5WS&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B0030CVQJY/?coliid=I31W0OBE9RPJJ2&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B0192CTMYG/?coliid=I1DII9YB3JOBQY&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00FPQA4KK/?coliid=IXUQC4EQV60LU&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01C3LHS1C/?coliid=I3KBALGR2X583N&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01LL8BU6M/?coliid=I27CV4O8FE4XYQ&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B075CT6XHW/?coliid=I39B943IVNYZP&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B079543TH1/?coliid=I2ZMIC0Y3GQG8&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07PBJTCRD/?coliid=I1RHJOKQ2S88JO&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07N5J1XX5/?coliid=I2FAJBGZBEISB5&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01DCTHQV6/?coliid=I1KG2ERH93HMK5&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07V4G6G28/?coliid=IUXDYY7G8P8AK&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B003TO5838/?coliid=I2NING7EZB2BYO&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01M5IMF5J/?coliid=I1GKEZ9J7RXEWD&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B004UHL3ZU/?coliid=IMYX3062HQGMN&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01DVEZLZU/?coliid=IF9HQT1MI94BA&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07YK1PD91/?coliid=I26GMG683O3I64&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01BX7S0J6/?coliid=I2NGH2ZL3CRC49&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B0045I6TQM/?coliid=I2SR3XDUXCULM8&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07QCH7L1R/?coliid=IU4ZYXDFZADGN&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B0854BPK75/?coliid=I2ZMOL7TDD8A9N&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B0047Y171G/?coliid=I3UPSP63KMJX92&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00NS3TEEY/?coliid=IN8LCESYJ0I2B&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07RSJWN62/?coliid=II8LFE5R2QO47&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B003VTZTU8/?coliid=I3QW0LE0J45AHT&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B002LHRLO8/?coliid=I2KLNOIR7Q37XO&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07MCJ3XMZ/?coliid=I1XF52N6G7558Z&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B088KPK1Q1/?coliid=IJO544L4WFY95&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08543D4W9/?coliid=I1EL731W16FLU7&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B079VVNP7P/?coliid=I1K6FI4MA0786U&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01E4DC6B4/?coliid=I2A4FAXCVNUU04&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B003OUXEDI/?coliid=I20ZNE6ZWYUHNX&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B008BU6X2U/?coliid=I28BZ517BH3LJ8&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00UNZYWKG/?coliid=I2IAG470GDSRHO&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00P42WWY6/?coliid=I4JHEU9Z112U8&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07H29BQLK/?coliid=I1I4QBDX00DMFJ&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B000FBJDDY/?coliid=I329Q23IS5U7QI&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00HY09XGQ/?coliid=I31568A3RP167A&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07VF1VQGR/?coliid=I2328FA168CSPB&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B000FC1BME/?coliid=I2OL5CCDM8J2ZW&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B019MMUA8S/?coliid=I3RTU0Z3LUPQ4W&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07L8NBCNG/?coliid=I2K1PT7D9CVTZO&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07GBKD8QM/?coliid=I238YLAUYZ67CU&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07173C875/?coliid=I1EOZ5N436CDH&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B007SGM2FU/?coliid=IWQ9V9Z4CD5RY&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00P42WWAA/?coliid=I2OJ7T1NSFHGIK&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01N6ACK3B/?coliid=I21NV5XD2D52RD&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07Z41TTNK/?coliid=I36BOH9P84FR2F&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07VBW3C4C/?coliid=I3ONFKA3HKZ5YY&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08DMWR6BP/?coliid=I1XCJFMMABAMTD&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B000PC0S0K/?coliid=I30SFNVYQYJBWU&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07D23CFGR/?coliid=I2W2DKSLTSRP36&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B00589AYWW/?coliid=IFT458HEN5JL8&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B01J16LJQ2/?coliid=I3TW4RKUZARQ1B&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07X16MWK9/?coliid=ICMN8JFM3ZH93&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07PWYFGY6/?coliid=I71Z32XX9Y8WV&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07N4C6LGR/?coliid=I2MNWYURPCWLPJ&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B006YDIYNC/?coliid=I313N2CXMYJ3UX&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07D6C6P29/?coliid=I3JI3GCKKGCUBM&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B084V936F9/?coliid=I1YPRT8PYRP4M1&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B089S7FPLB/?coliid=IS4O1O0F00XT3&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08BYWH6CS/?coliid=I1TBHACVGEABB7&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08KPJW7L9/?coliid=I92H89GVOZRL2&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08FHBLWLN/?coliid=I2PMPZX2E2NKOJ&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08KRG4S1Z/?coliid=I17DV9ZWQSPWUG&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B007GBTA5W/?coliid=I3PGQN7OVWL1GX&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B08Y8LBCLH/?coliid=I1G79Q7KISQAZ4&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B0055PJ4R0/?coliid=I1GXCLOBAF0U42&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B019B6TVZI/?coliid=I2UQFF8XI61VFJ&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B082S2TG11/?coliid=IQSO4XY1UJUGV&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07V5KKSZT/?coliid=I1EWXE8KQON0DR&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it", "https://www.amazon.com/dp/B07V327P61/?coliid=I2U4UMP36D1549&colid=35QH7NCHBH01U&psc=0&ref_=lv_ov_lig_dp_it"]

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36", "Referer" : "https://www.google.com"}

price_threshold = {}
not_buying = 0

def check_all():
    for URL in URLs:
        check_price(URL)
    print(price_threshold)
    send_mail(price_threshold)


def check_price(URL):
    # none_test(URL)
    """
    When Running the none_test(), comment out everything below this
    line for the rest of the function.
    """
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="kindle-price").get_text()
    
    converted_price = float(price[2:])

    if (converted_price <= 3.99):
        dict_index = len(price_threshold)
        dict_title = title.strip()
        dict_price = converted_price
        price_threshold[dict_index] = {"Title": dict_title, "Price": dict_price, "URL": URL}

    else:
        global not_buying
        not_buying = not_buying + 1


def send_mail(dict):
    """
    Puts together all the pieces and sends the email via the smtplib module.
    """

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # If posting online, make sure to hide the password here
    server.login("craigmenne@gmail.com", "jecxprwcmsfgsnse")
    subject = "Price Checker is working"
    body = build_email(price_threshold)

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "craigmenne@gmail.com",
        "craigmenne@gmail.com",
        msg
    )

    print("Email has been sent!")

    server.quit()


def build_email(dict):
    """
    Takes the dictionary and creates the body of the email.
    """

    body = ""

    if len(price_threshold) <=  7:
        body = body + "Nothing new to report here, But here are the usuals anyway:" + "\n\n"
    else:
        body = body + "It appears there was a new item addition. Please check carefully!" + "\n\n"

    for id, info in price_threshold.items():
        for key in info:
            body = body + "  " + str(info[key])
        body = body + "\n\n"

    return body


def none_test(URL):
    """
    Used to check if any of the URLs are a None Type. This would happen
    largely right now if the price is not listed as kindle-price in the
    html of the book URL.
    """

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="kindle-price")
    if price is None:
        print(URL)



check_all()
