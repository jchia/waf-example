top = '.'
out = 'build'
APPNAME = 'test'
VERSION = '0.0'

def options(opt):
    opt.load('compiler_cxx')
    opt.add_option('--mysdk', default='.', help='Path of some SDK.');

def configure(cfg):
    cfg.check_waf_version(mini='1.7.5')
    cfg.load('compiler_cxx')
    mysdk = cfg.options.mysdk
    cfg.env.MY_MYSDK = mysdk
    cfg.env.append_value('CXXFLAGS', ['-std=c++11', '-g'])
    cfg.check(features='cxx cxxprogram', lib=['pthread'], uselib_store='PTHREAD')
    cfg.env.append_value('LINKFLAGS_MYSDK', mysdk + '/mysdk.so')
    cfg.load('python')
    cfg.check_python_version((2,7,3))
    cfg.check_python_headers()
    cfg.env.LINKFLAGS_PYEXT_MYSDK = cfg.env.LINKFLAGS_PYEXT
    cfg.env.append_value('LINKFLAGS_PYEXT_MYSDK', mysdk + '/mysdk.so')

def build(bld):
    bld(name='myInclude', export_includes=[bld.env.MY_MYSDK, 'include'])
    bld.recurse('app foo bar')

# Have all 'cxx' targets have 'include' in their include paths.
from waflib import TaskGen
@TaskGen.taskgen_method
@TaskGen.feature('cxx')
def add_include(self):
    self.use = self.to_list(getattr(self, 'use', [])) + ['myInclude']
