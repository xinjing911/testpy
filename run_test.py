# 导包  时间包  结果报告包HT
import unittest
import common.HTMLTestRunnerNew as HT
import time
# 实例化套件
suite = unittest.TestSuite()
# 发现 文件夹下面的用例  添加到套件中
load = unittest.defaultTestLoader
cases = load.discover('test_cases',pattern='test*.py',top_level_dir=None)
suite.addTests(cases)
# 获得当前时间
currentTime = time.strftime('%Y_%m_%d %H-%M-%S')
# 设置测试报告的路径和文件名
filename = r'report/result_'+currentTime+'.html'
# 利用套件执行生成测试报告
with open(filename,'wb+') as fp:
    runner = HT.HTMLTestRunner(stream=fp,title="学生管理系统测试用例",description='babala',tester='xj')
    runner.run(suite)