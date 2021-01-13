import requests
import unittest
import json
class Sousuo_lcgl(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_01lclbss(self):  # 模糊搜索-正常搜索流程类别
        url = "http://123.57.140.190/manage/list_lc.php"
        ww = '原料'
        headers = {
            'Cookie': 'PHPSESSID=8mhnb0drtk2fm16ehod62pk7b0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        bb = requests.post(url=url, headers=headers, data=json.dumps(ww)).text
        self.assertIn("原料", bb, msg="断言失败")

    def test_02lclbss(self):  # 全名搜索-正常搜索流程类别
        url = "http://123.57.140.190/manage/list_lc.php"
        ww = '花牛苹果装箱追踪'
        headers = {
            'Cookie': 'PHPSESSID=8mhnb0drtk2fm16ehod62pk7b0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        bb = requests.post(url=url, headers=headers, data=json.dumps(ww)).text
        self.assertIn("花牛苹果装箱追踪", bb, msg="断言失败")

    def test_03lclbss(self):  # 不存在名称-搜索流程类别
        url = "http://123.57.140.190/manage/list_lc.php"
        ww = '打算开饭乐师傅；暗示法；啊'
        headers = {
            'Cookie': 'PHPSESSID=8mhnb0drtk2fm16ehod62pk7b0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        bb = requests.post(url=url, headers=headers, data=json.dumps(ww)).text
        self.assertNotIn("打算开饭乐师傅；暗示法；啊", bb, msg="断言失败")

    def test_04lclb(self):#模糊搜素物流码
        url="http://123.57.140.190/manage/list_lcsy.php"
        headers={
            "Cookie":"PHPSESSID=10rckm92rat69jkbamfhpr14m5",
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data={"txm":"NEN"}
        re=requests.post(url=url,headers=headers,data=data).text
        self.assertIn("NEN",re,msg="断言失败")

    def test_05lclb(self):#物流码全名搜素
        url="http://123.57.140.190/manage/list_lcsy.php"
        headers={
            "Cookie":"PHPSESSID=10rckm92rat69jkbamfhpr14m5",
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data={"txm":"55125415"}
        re=requests.post(url=url,headers=headers,data=data).text
        self.assertIn("55125415",re,msg="断言失败")

    def test_06lclb(self):#输入不存在的物流码搜素
        url="http://123.57.140.190/manage/list_lcsy.php"
        headers={
            "Cookie":"PHPSESSID=10rckm92rat69jkbamfhpr14m5",
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data={"txm":"dsaldskadkadnadsada"}
        re=requests.post(url=url,headers=headers,data=data).text
        self.assertNotIn("dsaldskadkadnadsada",re,msg="断言失败")
if __name__ == '__main__':
    vv=unittest.TestSuite()
    vv.addTest(Sousuo_lcgl('test_06lclb'))
    # vv.addTest(Sousuo_lcgl('test_02lclbss'))
    # vv.addTest(Sousuo_lcgl('test_03lclbss'))
    gg=unittest.TextTestRunner(verbosity=2)
    gg.run(vv)






