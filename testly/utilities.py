import yaml
import errno
import __main__

class YAMLReader:
    def read(self,filename):
        try:
            with open(filename) as file:
                instruction_dict = yaml.load(file, Loader=yaml.FullLoader)
                print(instruction_dict)
                return instruction_dict
        except:
            raise FileNotFoundError(errno.ENOENT, __main__.os.strerror(errno.ENOENT), filename)
        
    def validateYAML(self):
        pass
    # def checkExist(self, filename):
    #     pass
    
    def writeFile(self, filename):
        pass