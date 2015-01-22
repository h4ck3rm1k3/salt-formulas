
class Salt:
    pass

class Grains:
    def __init__(self):
        self.os="Debian"
        self.kernel="Linux"
    def filter_by(self,x=None, merge=None, c=None):
        print "Filterby",x, merge, c
        return x['Debian']


class Pillar:
    def __init__(self):
        self.data = {
            'tomcat:sites' : { "funky"  : "cold"}       ,
            'tomcat:version' : 5,
            'tomcat:lookup' : True,
            'java:home' : '/usr',
            'java:Xmx': '3G',
            'java:MaxPermSize': '256m',
            'java:UseConcMarkSweepGC' : False,
            'java:CMSIncrementalMode' : False,
            'tomcat:security' : True,
            'limit:soft' : True, 

        }

    def get(self,x, default=None):
        print "Pillar.get key='{0}' default='{1}'".format(x, default)
        if x in self.data:
            v = self.data[x]
            print "Pillar.get found key='{0}' value='{1}'".format(x, v)
            return v
        else:
            return default


class Opts(object):

    def __init__(self, data) :
        self.data=data
    # def keys(self): return self.data.keys()
    # def has_key(self, key): return key in self.data

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        if hasattr(self.__class__, "__missing__"):
            return self.__class__.__missing__(self, key)
        raise KeyError(key)

    def __contains__(self, key):
        return key in self.data

    def get(self, item, default):
        print "get item", item            
        return self.data[item]
    def items(self): return self.data.items()
    def iteritems(self): return self.data.iteritems()
    def iterkeys(self): return self.data.iterkeys()
    def itervalues(self): return self.data.itervalues()
    def __setitem__(self, key, item): self.data[key] = item


class TomCat:
    def native(self, x):
        return "True"
