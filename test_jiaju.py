import pytest
from Pytest.ceshijiaju import jiaju1, jiaju2,jiaju3
from time import sleep
@pytest.mark.login
class Testlogin():
    def test_login(self,jiaju1,jiaju2,jiaju3):
        print("sss")
        # 这里的driver就是夹具返回的driver（就是参数接收），注意不能有括号；
        dd = jiaju1
        a = jiaju2
        x,y=jiaju3
        print("夹具内部调用的值：",x,y)
        print(a)
        print(dd)
        d=dd[0]
        print("得到测试夹具2的返回值，进行关联",len(a),a)
        d.get("http://219.141.235.67:18603/login")
        d.implicitly_wait(10)
        account = d.find_element_by_xpath("//input[@placeholder='登录账号']")
        account.click()
        account.clear()
        account.send_keys("zhangbinghui")
        passwd = d.find_element_by_xpath("//input[@placeholder='密码']")
        passwd.click()
        passwd.clear()
        passwd.send_keys("123456")
        d.find_element_by_xpath(
            "//button[@class='el-button login-button el-button--default el-button--small']").click()
        sleep(10)
        assert "张冰辉" in d.page_source
        print("打开成功")
if __name__ == "__main__":
    pytest.main(["-vs","test_jiaju.py"])

