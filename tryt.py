class Test:
    def method1(self):
        return 'howdy python'
    def method2(self, methodToRun):
        result = methodToRun()
        return result
    def method3(self):
        return self.method2(self.method1)
test = Test()
print test.method3() 
