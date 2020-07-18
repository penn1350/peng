
class Page(object):
    """

    页面基础类，用于所有页面的继承
    """
    bs_url = "http://bbs.meizu.cn"
    def __init__(self,selenium_driver,base_url= bs_url,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent
    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(),"Did not land on %s" % url
    def find_element(self,*loc):
        return self.driver.
